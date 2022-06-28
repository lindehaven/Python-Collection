'''Onboard Computer Energy Unit (OBCEU)

Author : Lars Lindehaven
Date   : 2019-06-03
'''
# pylint: disable=invalid-name,global-statement,protected-access

# Imports
import pickle

# Constants
_DATA_FILE = 'obceu.p'
_MAX_BATTERY_CAPACITY = 200.0 # 200 kWh maximum capacity
_STATIC_POWER_CONSUMPTION = 0.1 # 100 W consumption for lights and computers

# Persistent data
_total_time = 0.0
_total_energy = 0.0
_remaining_energy = 0.0


def _load_from_file():
    '''Loads persistent data from file'''
    global _total_time
    global _total_energy
    global _remaining_energy
    try:
        fd = open(_DATA_FILE, 'rb')
        data = pickle.load(fd)
        fd.close()
        _total_time = data[0]
        _total_energy = data[1]
        _remaining_energy = data[2]
    except FileNotFoundError:
        _save_to_file()


def _save_to_file():
    '''Saves persistent data from file'''
    fd = open(_DATA_FILE, 'wb')
    data = [_total_time, _total_energy, _remaining_energy]
    pickle.dump(data, fd)
    fd.close()


def _sampled(tsps, flwd, frwd, rlwd, rrwd):
    '''Reduces battery energy depending on current speed.

    Arguments
    ---------
        tsps : float
            Time since previous sample in seconds [s].
        flwd : float
            Front left wheel distance in meters [m].
        frwd : float
            Front right wheel distance in meters [m].
        rlwd : float
            Rear left wheel distance in meters [m].
        rrwd : float
            Rear right wheel distance in meters [m].

    Returns
    -------
        _sampled : bool
            True if battery energy remains.
            False if no battery energy remains.
    '''
    global _total_time
    global _total_energy
    global _remaining_energy
    outcome = True
    if tsps > 0.0:
        # Load persistent data
        _load_from_file()
        # Shortest distance that a wheel has travelled
        shortest = min(abs(flwd), abs(frwd), abs(rlwd), abs(rrwd))
        # Longest distance that a wheel has travelled
        longest = max(abs(flwd), abs(frwd), abs(rlwd), abs(rrwd))
        # Average distance that the wheels have travelled
        distance = (shortest + longest) / 2
        # Calculate current speed
        speed = distance / tsps
        # Calculate consumed energy
        energy = _STATIC_POWER_CONSUMPTION * tsps / 3600  + speed**1.2 / 56765
        # Increase accumulated time
        _total_time += tsps
        # Increase accumulated used energy and decrease battery level
        if energy <= _remaining_energy:
            _total_energy += energy
            _remaining_energy -= energy
        else:
            _total_energy += _remaining_energy
            _remaining_energy = 0
            outcome = False
        # Save persistent data
        _save_to_file()
    return outcome


def charge_battery_energy(percent):
    '''
    Charges batteries to a given percentage of the maximum energy capacity.

    Arguments
    ---------
        percent : float
            Percentage of the maximum energy capacity [%].

    Returns
    -------
        charge_battery_energy : bool
            True if successful.
            False if unsuccessful.
    '''
    global _remaining_energy
    outcome = False
    if 0.0 <= percent <= 100.0:
        _remaining_energy = percent*_MAX_BATTERY_CAPACITY/100.0
        _save_to_file()
        outcome = True
    return outcome


def maximum_battery_energy():
    '''
    Returns
    -------
        maximum_battery_energy : float
            Maximum battery energy in kilowatthours [kWh].
    '''
    return _MAX_BATTERY_CAPACITY


def remaining_battery_energy():
    '''
    Returns
    -------
        remaining_battery_energy : float
            Remaining battery energy in kilowatthours [kWh].
    '''
    return _remaining_energy

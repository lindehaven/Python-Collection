'''Onboard Computer Calculation Unit (OBCCU)

Author : Lars Lindehaven
Date   : 2019-06-05
'''
# pylint: disable=global-statement,invalid-name,protected-access

# Imports
import pickle
import obcdu
import obceu

# Constants
_DATA_FILE = 'obccu.p'
NOMINAL_RANGE_PER_KWH = 3_000

# Non-persistent data
_previous_speed = 0.0
_current_speed = 0.0
_spin_warning = False
_skid_warning = False

# Persistent data
_total_time = 0.0
_total_distance = 0.0
_total_energy = 0.0
_remaining_energy = 0.0


def _load_from_file():
    '''Loads persistent data from file'''
    global _total_time
    global _total_distance
    global _total_energy
    global _remaining_energy
    try:
        fd = open(_DATA_FILE, 'rb')
        data = pickle.load(fd)
        fd.close()
        _total_time = data[0]
        _total_distance = data[1]
        _total_energy = data[2]
        _remaining_energy = data[3]
    except FileNotFoundError:
        _save_to_file()


def _save_to_file():
    '''Saves persistent data from file'''
    fd = open(_DATA_FILE, 'wb')
    data = [_total_time,
            _total_distance,
            _total_energy,
            _remaining_energy]
    pickle.dump(data, fd)
    fd.close()


def average_power_consumption():
    '''
    Arguments
    ---------
        None

    Returns
    -------
        average_power_consumption : int
            Average power consumption in kilowatts [kW].
            None if not implemented.
    '''
    avg_power = 0
    if _total_time > 0.0:
        avg_power = _total_energy * 3600.0 / _total_time
    return int(avg_power + 0.5)


def average_speed():
    '''
    Arguments
    ---------
        None

    Returns
    -------
        average_speed : int
            Average speed in kilometers per hour [km/h].
            None if not implemented.
    '''
    avg_speed = 0
    if _total_time > 0.0:
        avg_speed = _total_distance / _total_time * 3.6
    return int(avg_speed + 0.5)


def current_speed():
    '''
    Arguments
    ---------
        None

    Returns
    -------
        current_speed : int
            Current speed in kilometers per hour [km/h].
            None if not implemented.
    '''
    return int(_current_speed * 3.6 + 0.5)


def remaining_distance():
    '''
    Arguments
    ---------
        None

    Returns
    -------
        remaining_distance : int
            Remaining distance in meters [m] using remaining energy.
            None if not implemented.
    '''
    rem_energy = obceu.remaining_battery_energy() # [kWh]
    rem_dist = rem_energy * NOMINAL_RANGE_PER_KWH
    return int(rem_dist)


def sampled(tsps, flwd, frwd, rlwd, rrwd):
    '''Receives wheel distances for all four wheels at a given sample time.

    Calculates travelled distance, remaining distance using remaining energy,
    current speed, average speed, average power consumption, wheel spin warning
    and wheel skid warning.

    Time since previous sample is nominally 0.1s.

    Wheel distance is positive when the wheel rotates forward and wheel
    distance is negative when the wheel rotates backward.

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
      sampled : bool
        True if successful calculation.
        False if unsuccessful calculation.
        None if not implemented.
    '''
    global _current_speed
    global _previous_speed
    global _total_time
    global _total_distance
    global _total_energy
    global _remaining_energy
    global _skid_warning
    global _spin_warning
    outcome = False
    if tsps > 0.0:
        # Load persistent data
        _load_from_file()
        # Shortest distance that a wheel has travelled
        shortest = min(abs(flwd), abs(frwd), abs(rlwd), abs(rrwd))
        # Longest distance that a wheel has travelled
        longest = max(abs(flwd), abs(frwd), abs(rlwd), abs(rrwd))
        # Average distance that the wheels have travelled
        distance = (shortest + longest) / 2
        # Save current speed to be able to calculate acceleration/retardation
        _previous_speed = _current_speed
        # Calculate and save current speed
        _current_speed = distance / tsps
        # Calculate acceleration (positive) or retardation (negative)
        acceleration = (_current_speed - _previous_speed) / tsps
        # A normal U turn would result in the outer wheels travelling further
        # than the inner wheels; up to 30-40%. If any of the wheels travel even
        # further (50% or more) then it most probably skids or spins.
        _spin_warning = False
        _skid_warning = False
        if 1.5 * shortest < longest:
            # If the vehicle is retarding, the wheel(s) skid
            if acceleration < 0.0:
                _skid_warning = True
            # If the vehicle is accelerating, the wheel(s) spin
            elif acceleration > 0.0:
                _spin_warning = True
        # Calculate consumed energy
        current_remaining_energy = obceu.remaining_battery_energy()
        consumed_energy = _remaining_energy - current_remaining_energy
        if consumed_energy < 0.0:
            consumed_energy = 0.0
        _remaining_energy = current_remaining_energy

        # Increase accumulated time
        _total_time += tsps
        # Increase accumulated distance
        _total_distance += distance
        # Increase accumulated energy
        _total_energy += consumed_energy
        # Save persistent data
        _save_to_file()
        outcome = True
        # Display to driver
        obcdu._display(travelled_distance(),
                       remaining_distance(),
                       current_speed(),
                       average_speed(),
                       average_power_consumption(),
                       wheel_skid_warning(),
                       wheel_spin_warning(),
                       int(_total_time + 0.5),
                       int(current_remaining_energy + 0.5)
                       )
    return outcome


def travelled_distance():
    '''
    Arguments
    ---------
        None

    Returns
    -------
        travelled_distance : int
            Travelled distance in meters [m].
            None if not implemented.
    '''
    return int(_total_distance + 0.5)


def wheel_skid_warning():
    '''
    Arguments
    ---------
        None

    Returns
    -------
        wheel_skid_warning : bool
            True if one, two or three wheels skid.
            False if no wheel skids.
            None if not implemented.
    '''
    return _skid_warning


def wheel_spin_warning():
    '''
    Arguments
    ---------
        None

    Returns
    -------
        wheel_spin_warning : bool
            True if one, two or three wheels spin.
            False if no wheel spins.
            None if not implemented.
    '''
    return _spin_warning

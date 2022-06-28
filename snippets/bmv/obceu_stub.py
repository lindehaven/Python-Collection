'''Onboard Computer Energy Unit (OBCEU) Stub

Author : Lars Lindehaven
Date   : 2019-06-04

This module is a stub for the real Onboard Computer Energy Unit (OBCEU).

PLEASE NOTE THAT:
-- A stub is intended for early integration of the system.
-- A stub provides the real interface but returns fake values.
-- A stub is not the real thing!
-- A stub is a faked, counterfeit, falsified, imaginary friend.
-- To use this stub module during integration : import obceu_stub
-- To use the real module before delivery : import obceu

'''
# pylint: disable=invalid-name,global-statement,protected-access

# Constants
_MAX_BATTERY_CAPACITY = 10.0 # 10 kWh maximum capacity

# Non-persistent data
_remaining_energy = _MAX_BATTERY_CAPACITY


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
    # Oh no, no boundary check! The sky is the limit.
    _remaining_energy = percent * _MAX_BATTERY_CAPACITY / 100.0
    return True


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
    global _remaining_energy
    _remaining_energy -= 1.0 # Fake it 'til you make it!
    if _remaining_energy < 0:
        _remaining_energy = 0.0
    return _remaining_energy

'''Onboard Computer Wheel Unit (OBCWU)

Author : Lars Lindehaven
Date   : 2019-05-22
'''
# pylint: disable=protected-access

# Imports
import argparse
import sys
import time
import obccu
import obceu


def _main():
    '''Reads sample data and sends to control unit'''

    parser = argparse.ArgumentParser(description='OBC Wheel Unit')
    parser.add_argument('--charge', dest='level', type=float,
                        help='charge battery in percent (0-100)')
    parser.add_argument('--wait', dest='time', type=float,
                        help='wait time in seconds (0-10)')
    args = parser.parse_args()
    if args.level is not None:
        obceu.charge_battery_energy(args.level)
    if args.time is None or args.time < 0.0 or args.time > 10.0:
        args.time = 0.0

    for in_data in sys.stdin.readlines():
        try:
            arg = [float(element) for element in in_data.strip().split()]
            time.sleep(args.time)
            if obceu._sampled(arg[0], arg[1], arg[2], arg[3], arg[4]):
                # Still some energy in the battery so let the vehicle run
                obccu.sampled(arg[0], arg[1], arg[2], arg[3], arg[4])
            else:
                # Oooops, no more battery energy so stop the vehicle!
                obccu.sampled(arg[0], 0.0, 0.0, 0.0, 0.0)
        except IndexError:
            pass

if __name__ == '__main__':
    _main()

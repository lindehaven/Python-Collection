'''Circle

Provides functions for calculating properties of circles.
'''

from math import pi

def area(radius):
    '''Calculates the area of a circle.'''
    return abs(radius) * abs(radius) * pi

def circ(radius):
    '''Calculates the circumference of a circle.'''
    return 2 * abs(radius) * pi

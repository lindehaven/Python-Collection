'''Rectangle

Provides functions for calculating properties of rectangles.
'''

def area(length, width):
    '''Calculates the area of a rectangle.'''
    return abs(length) * abs(width)

def circ(length, width):
    '''Calculates the circumference of a rectangle.'''
    return 2 * (abs(length) + abs(width))

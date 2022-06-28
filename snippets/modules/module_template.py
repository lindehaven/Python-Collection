'''Module Template

Gives a base for developing Python modules.
'''

# First the imports, for example:
from math import pi

# Then the functions, for example these:
def area(radius):
    '''Calculates the area of a circle'''
    return abs(radius) * abs(radius) * pi

def circumference(radius):
    '''Calculates the circumference of a circle'''
    return 2 * abs(radius) * pi

def main():
    '''Asks user for radius and prints circumreference and area'''
    while True:
        try:
            radius = float(input('Radien på cirkeln? '))
            break
        except ValueError:
            print('Kunde inte beräkna arean, försök igen.')
    print('Cirkelns omkrets blir', circumference(radius))
    print('Cirkelns area blir', area(radius))

# Finally the code for executing as main, for example:
if __name__ == '__main__':
    main()

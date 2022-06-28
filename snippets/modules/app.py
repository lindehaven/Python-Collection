'''Modules and Functions Assignment

Main application with menu to choose operation.
'''

import mathematics
import rectangle
import circle

EXIT = 0
MATH_ADD = 1
MATH_SUB = 2
MATH_MUL = 3
MATH_DIV = 4
RECT_AREA = 5
RECT_CIRC = 6
CIRC_AREA = 7
CIRC_CIRC = 8
LAST = 9

def main():
    '''Prints results of functions and values that are chosen by user.'''
    choice = menu_choice()
    while choice != EXIT:
        print_result(choice)
        choice = menu_choice()

def menu_choice():
    '''Prints the menu and waits for the user to choose. Returns choice.'''
    while True:
        try:
            print('----')
            print('Menu')
            print('----')
            print(EXIT, ': Exit')
            print(MATH_ADD, ': Addition')
            print(MATH_SUB, ': Subtraction')
            print(MATH_MUL, ': Multiplication')
            print(MATH_DIV, ': Division')
            print(RECT_AREA, ': Rectangle area')
            print(RECT_CIRC, ': Rectangle circumference')
            print(CIRC_AREA, ': Circle area')
            print(CIRC_CIRC, ': Circle circumference')
            choice = int(input('Please enter a number: '))
            if choice >= EXIT and choice < LAST:
                break
        except ValueError:
            print('Invalid choice, please try again.')
    return choice

def input_value(text):
    '''Gets a value from the user. Returns the value.'''
    while True:
        try:
            value = float(input(text))
            break
        except ValueError:
            print('Invalid value, please try again.')
    return value

def print_result(choice):
    '''Calls appropriate function in appropriate module.'''
    if choice == MATH_ADD:
        print('Sum =', mathematics.add(input_value('Term 1? '),
                                       input_value('Term 2? ')))
    elif choice == MATH_SUB:
        print('Difference =', mathematics.sub(input_value('Term 1? '),
                                              input_value('Term 2? ')))
    elif choice == MATH_MUL:
        print('Product =', mathematics.mul(input_value('Factor 1? '),
                                           input_value('Factor 2? ')))
    elif choice == MATH_DIV:
        print('Quotient =', mathematics.div(input_value('Numerator? '),
                                            input_value('Denominator? ')))
    elif choice == RECT_AREA:
        print('Area =', rectangle.area(input_value('Length? '),
                                       input_value('Width? ')))
    elif choice == RECT_CIRC:
        print('Circumference =', rectangle.circ(input_value('Length? '),
                                                input_value('Width? ')))
    elif choice == CIRC_AREA:
        print('Area =', circle.area(input_value('Radius? ')))
    elif choice == CIRC_CIRC:
        print('Circumference =', circle.circ(input_value('Radius? ')))

if __name__ == '__main__':
    main()

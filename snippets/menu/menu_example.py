'''Menu Example

Gives an example of how to build a simple menu.
'''

import circle
# Add more imports here ...

EXIT = 0
CIRCLE_AREA = 1
CIRCLE_CIRC = 2
# Add more menu choices here ...
LAST = 3 # Increase this when you add menu choices above

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
            print(CIRCLE_AREA, ': Circle area')
            print(CIRCLE_CIRC, ': Circle circumference')
            # Add more menu choices here ...
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
    '''Calls appropiate function in appropriate module.'''
    if choice == CIRCLE_AREA:
        print('Area =', circle.area(input_value('Radius? ')))
    elif choice == CIRCLE_CIRC:
        print('Circumference =', circle.circ(input_value('Radius? ')))
    # Add more conditions and function calls here ...

if __name__ == '__main__':
    main()

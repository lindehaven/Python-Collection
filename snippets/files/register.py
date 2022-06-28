'''Register

Uses a dictionary to store a register of names and e-mail addresses. Loads and
saves the register in a pickled file for persistency and security reasons.
'''

import pickle

# Menu functions
EXIT = 0
CHANGE = 1
SEARCH = 2
REMOVE = 3
DISPLAY = 4
LAST = 5 # Keep last as sentinel

def load(file):
    '''Loads the register from file and returns the register'''
    try:
        register = pickle.load(open(file, "rb"))
        print('OK. Läst från '+file)
    except FileNotFoundError:
        register = {}
        save(file, register)
    return register

def save(file, register):
    '''Saves the register to file'''
    pickle.dump(register, open(file, "wb"))
    print('OK. Sparat i '+file)

def menu():
    '''Prints the menu, waits for the user to choose and returns choice'''
    while True:
        print()
        print('Vad vill du göra?')
        print('=================')
        print(EXIT, ': Avsluta')
        print(CHANGE, ': Lägga till eller ändra en adress')
        print(SEARCH, ': Söka en adress')
        print(REMOVE, ': Ta bort en adress ur listan')
        print(DISPLAY, ': Visa hela registret')
        print('Välj', EXIT, '-', DISPLAY, end=': ')
        try:
            choice = int(input())
            if LAST > choice >= EXIT:
                break
        except ValueError:
            print('Felaktigt val.')
    return choice

def email_ok(adress):
    '''Checks e-mail address, returns True if successful'''
    if not '@' in adress:
        return False
    part1 = adress.split('@')
    if not part1[0]:
        return False
    if not '.' in part1[1]:
        return False
    part2 = part1[1].split('.')
    if not part2[0] or len(part2[1]) < 2:
        return False
    return True

def change(register):
    '''Changes or enters item in the register, returns True if successful'''
    name = input('Ange namn: ').title()
    if not name:
        return False
    email = input('Ange e-postadress: ').lower()
    if not email:
        return False
    while not email_ok(email):
        print('Felaktig e-postadress')
        email = input('Ange e-postadress: ').lower()
        if not email:
            return False
    register[name] = email
    return True

def search(register):
    '''Searches item in the register, returns True if successful'''
    name = input('Vem söker du? ').title()
    if name and name in register.keys():
        print(name+' har e-postadress: '+register[name])
        return True
    print('Hittar inte '+name+' i registret')
    return False

def remove(register):
    '''Removes item from the register, returns True if successful'''
    name = input('Vem vill du ta bort? ').title()
    if name and name in register.keys():
        del register[name]
        print('Tog bort '+name+' från registret')
        return True
    print('Hittar inte '+name+' i registret')
    return False

def display(register):
    '''Displays all items in the register, returns True if successful'''
    if  register:
        for name in sorted(register.keys()):
            print(name+', '+ register[name])
        return True
    print('Registret är tomt')
    return False

def main():
    '''Loads register and performs user actions on the register'''
    file = 'register.p'
    register = load(file)
    chosen = menu()
    while chosen:
        if chosen == CHANGE:
            if change(register):
                save(file, register)
        elif chosen == SEARCH:
            search(register)
        elif chosen == REMOVE:
            if remove(register):
                save(file, register)
        elif chosen == DISPLAY:
            display(register)
        chosen = menu()

if __name__ == '__main__':
    main()

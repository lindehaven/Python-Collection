'''fakultet

Beräknar n! genom att använda rekursion.
'''

def fakultet(n):
    '''Rekursiv funktion för beräkning av fakultet'''
    if n <= 1:
        return 1
    else:
        return n*fakultet(n-1)

if __name__ == '__main__':
    print('Tal'.rjust(6) + 'Fakultet'.rjust(10))
    for i in range(1, 11):
        print(str(i).rjust(6) + str(fakultet(i)).rjust(10))

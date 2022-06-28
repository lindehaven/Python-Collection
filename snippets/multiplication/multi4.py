'''Utökad Multiplikationstabell med två funktioner

Bygg om ditt program från uppgiften "Utökad Multiplikationstabell med funktion".

Lägg till ytterligare en funktion som heter print_table och som tar två argument
first och last. Funktionen ska innehålla en for-loop som repeterar från och med
last till och med last. För varje repetition ska funktionen print_row anropas så
att samma utskrifter fås som i uppgiften "Utökad Multiplikationstabell med
funktion".
'''

def print_row(x): # Funktion med ett argument x
    for c in range(1, 10): # Iteration begränsad till {1..9}
        print("{:3d}".format(c*x), end=', ') # Komma mellan talen
    print("{:3d}".format(10*x)) # Inget komma på slutet av raden

def print_table(first, last): # Funktion med två argument first och last
    if first >= 1 and first <= 99 and last <= 99: # Kolla först värdeområdet
        for number in range(first, last+1): # Iteration begränsad till {m..n}.
            print_row(number) # Anropa funktionen print_row med värdet på x

if __name__ == '__main__':
    m = int(input("m? ")) # Läser in m som ett heltal
    n = int(input("n? ")) # Läser in n som ett heltal
    print_table(m, n) # Anropa funktionen print_table med värden på first och last

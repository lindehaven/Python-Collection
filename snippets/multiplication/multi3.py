'''Utökad Multiplikationstabell med funktion

Bygg om ditt program från uppgiften "Utökad Multiplikationstabell".

Lägg till en funktion som heter print_row och som tar ett argument x. Funktionen
ska skriva ut multiplikationstabellen för x på en rad med komman mellan
produkterna. Anropa funktionen med rätt värden på x för att få samma utskrifter
som i uppgiften "Utökad Multiplikationstabell".
'''

def print_row(x): # Definiera funktion med ett argument x
    for c in range(1, 10): # Iteration begränsad till {1..9}
        print("{:3d}".format(c*x), end=', ') # Komma mellan talen
    print("{:3d}".format(10*x)) # Inget komma på slutet av raden

m = int(input("m? ")) # Läser in m som ett heltal
n = int(input("n? ")) # Läser in n som ett heltal
if m >= 1 and m <= 99 and n <= 99: # Kolla först värdeområdet
    for number in range(m, n+1): # Iteration begränsad till {m..n}.
        print_row(number) # Anropa funktionen print_row med värdet på x

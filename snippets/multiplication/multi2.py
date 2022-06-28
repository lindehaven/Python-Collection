'''Utökad Multiplikationstabell

Skriv ett Python-program som:
Läser in ett heltal m från tangentbordet där m = {1..99}.
Läser in ett heltal n från tangentbordet där n = {m..99}.
Skriver ut multiplikationstabellen för alla tal mellan m till n.
Om till exempel m = 1 och n = 3 så ska följande skrivas ut:
 1,  2,  3,  4,  5,  6,  7,  8,  9, 10
 2,  4,  6,  8, 10, 12, 14, 16, 18, 20
 3,  6,  9, 12, 15, 18, 21, 24, 27, 30
Notera att alla tal ska vara högerjusterade.
'''

m = int(input("m? ")) # Läser in m som ett heltal
n = int(input("n? ")) # Läser in n som ett heltal
if m >= 1 and m <= 99 and n >= m and n <= 99: # Kolla först värdeområdet
    for x in range(m, n+1): # Yttre iteration begränsad till {m..n}.
        for c in range(1, 10): # Inre iteration begränsad till {1..9}
            print("{:3d}".format(c*x), end=', ') # Komma mellan talen
        print("{:3d}".format(10*x)) # Inget komma på slutet av raden
else:
    print('För högt eller för lågt värde!')

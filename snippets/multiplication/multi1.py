'''Multiplikationstabell

Skriv ett Python-program som:
Läser in ett heltal n från tangentbordet.
Skriver ut multiplikationstabellen för talet n.
Om till exempel n=3 så ska följande skrivas ut:
3, 6, 9, 12, 15, 18, 21, 24, 27, 30
'''

n = int(input("n? ")) # Läser in n som ett heltal
for factor in range(1, 10): # Iteration begränsad till {1..9}
    print(factor*n, end=', ') # Komma mellan talen
print(10*n) # Inget komma på slutet av raden

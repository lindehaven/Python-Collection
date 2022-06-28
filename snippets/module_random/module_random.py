import random
print(random.randint(1,6)) # Slumpa fram ett tal 1-6.
c = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] # En del av en kortlek.
for _ in range(7):         # Vi ska kupera korten sju gånger.
   random.shuffle(c)       # Kupera korten slumpmässigt. 
   print(c)                # Visa korten.

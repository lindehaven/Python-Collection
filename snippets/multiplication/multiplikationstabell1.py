# Multiplikationstabell 1

# Läs in den lägsta faktorn.
m = int(input("Vilket lägre heltal? "))

# Läs in den högsta faktorn.
n = int(input("Vilket högre heltal? "))

# Yttre loop för varje faktor y i multiplikationstabellen.
for y in range(m, n+1):

    # Inre loop för varje faktor x (där x=1..10).
    for x in range(1, 11):

        # Beräkna produkten en gång för vi kommer att
        # använda den fler gånger nedan.
        p = x*y

        # Högerjustera genom att skriva ut ett mellan-
        # slag först om produkten är ett ental.
        if p < 10:
            print(end=" ")

        # Skriv ut produkten y*x (där x=1..9) på en
        # rad med kommatecken mellan varje produkt...
        if x < 10:
            print(p, end=", ")

        # ...annars skriv ut produkten y*x (där x=10)
        # och flytta markören till en ny rad.
        else:
            print(p)
        

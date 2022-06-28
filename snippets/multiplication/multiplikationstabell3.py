# Multiplikationstabell 3

def print_mul(m, n):

    # Yttre loop för varje faktor y i multiplikationstabellen.
    for y in range(m, n+1):

        # Inre loop för varje faktor x (där x=1..10).
        for x in range(1, 11):

            # Beräkna produkten en gång för vi kommer att
            # använda den fler gånger nedan.
            p = x*y

            # Högerjustera genom att skriva ut rätt antal
            # mellanslag först. Rätt antal mellanslag fås
            # genom att beräkna antalet tecken i den
            # produkt som ska skrivas ut just nu, dvs p.
            # Sedan beräknas högsta antalet tecken som
            # kan förekomma i en produkt, dvs n*10.
            for s in range(len(str(p)), len(str(n*10))):
                print(end=" ")

            # Skriv ut produkten y*x (där x=1..9) på en
            # rad med kommatecken mellan varje produkt...
            if x < 10:
                print(p, end=", ")

            # ...annars skriv ut produkten y*x (där x=10)
            # och flytta markören till en ny rad.
            else:
                print(p)

# Läs in den lägsta faktorn.
m = int(input())

# Läs in den högsta faktorn.
n = int(input())

# Skriv ut multiplikationstabellen.
print_mul(m, n)

#   Skriv en funktion som räknar ut summan av alla positiva heltal tal från
#   1 till n och skickar tillbaka det.
#
# Analys
#   Vilka är indata?
#     Ett tal n som kan matas in via tangentbordet.
#   Vilket resultat förväntas?
#     Summan av alla positiva heltal 1..n.
#   Vad behöver vi?
#     En funktion som tar ett argument n, repeterar ett tal 1..n, adderar talet
#     till summan och returnerar summan.
#     Inmatning av talet n.
#     Anrop av funktionen.
#     Utskrift av summan.
#
def summa(n):
    s = 0
    for t in range(1, n+1):
        s = s + t
    return s
n = int(input('Tal: '))
print(summa(n))

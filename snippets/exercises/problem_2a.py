#   Vi har en funktion f(x) = 1/x för alla x skiljt från 0 (noll).
#   Visa att f(x) går mot oändligheten när x går mot noll.
#
# Analys
#   Vi ser på funktionen att x behöver vara väldigt liten för att gå mot
#   oändligheten men den får inte bli 0 (noll). Inom matematiken talar man
#   om att x har ett gränsvärde som är skiljt från 0 (noll). 
#   För att visa att funktionen går mot oändligheten behöver vi anropa
#   funktionen f(x) med ett x som blir mindre och mindre. Vi kan inse att
#   vi bör skapa en slinga för detta samt skriva ut både x och f(x). Vi vet
#   också att en for-loop inte kan använda decimaltal (float) så vi väljer
#   en while-loop istället.
#
def f(x):
    return 1/x
d = 1e-12
x = 1
while x >= d:
    print('x={:.12f}, f(x)={:.0f}'.format(x, f(x)))
    x = x / 2

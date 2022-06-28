#   Vi har en funktion m(x) = 3x - 7 och en funktion n(x) = -4x + 11.
#   Visa vilket värde på x som ger m(x) = n(x).
#
# Analys
#   Problemet är återigen av typen linjärt ekvationssystem som kan lösas genom
#   att prova en serie med värden på x och ser när m(x) blir lika med n(x).
#   Det gick ju bra när vi löste problem B så det kan ju gå bra även nu.
#
def m(x):
    return 3*x - 7
def n(x):
    return -4*x + 11
limit = 0.0005              # Felmarginalen är +/- 0.0005
adjust = limit/2            # Finjustering av x är hälften av felmarginalen
x = 2.5
while x < 2.6:
    minimum = m(x) - limit  # Lägsta acceptabla värdet för m(x)
    maximum = m(x) + limit  # Högsta acceptabla värdet för m(x)
    if minimum <= n(x) <= maximum:  # Ligger inom felmarginalen?
        print('x =', x, 'ger m(x) =', m(x), 'och n(x) =', n(x))
    x = x + adjust          # Vi finjusterar här


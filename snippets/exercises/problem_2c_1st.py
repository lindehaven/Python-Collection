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
for x in range(-5, 6):
    if m(x) == n(x):
        print('x =', x, 'ger m(x) = n(x) =', m(x))

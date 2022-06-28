#   Vi har en funktion f(x) = 3x - 5 och en funktion g(x) = -2x + 7.
#   Visa vilket värde på x som ger f(x) = g(x).
#
# Analys
#   Problemet är av typen linjärt ekvationssystem som kan lösas grafiskt genom
#   att rita x, f(x) och g(x) i samma koordinatsystem. Där funktionerna graf
#   skär varnadra finns lösningen. Det kan också lösas genom att pröva olika
#   värden på x tills dess f(x) blir lika med g(x).
#   Det är den senare metoden som vi ska använda när vi programmerar lösningen.
#   Vi provar helt enkelt en serie med värden på x och ser när f(x) blir lika
#   med g(x). Denna metod utan finess kallas "brute force".
#
def f(x):
    return 3*x - 4
def g(x):
    return -2*x + 6
for x in range(-5, 6):
    if f(x) == g(x):
        print('x =', x, 'ger f(x) = g(x) =', f(x))

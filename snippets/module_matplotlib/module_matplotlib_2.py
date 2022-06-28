from matplotlib.pyplot import *
def f(x):           # Definierar funktionen
    return x**2 - 5*x - 20
x = []              # Skapar en tom lista för kategorivärden på x-axeln
y = []              # Skapar en tom lista för funktionsvärden på y-axeln
for n in range(-9, 10):
    x.append(n)     # Lägger till kategorivärde
    y.append(f(n))  # Lägger till funktionsvärde
plot(x, y)          # Plottar kategori- och funktionsvärden
show()              # Visar grafen

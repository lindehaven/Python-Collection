# Uppgift 1:
# a) Funktioner för alla fyra räknesätten
# b) Funktion som ger medelvärdet av två värden
# c) Anrop av alla fem funktioer med olika värden
# d) Utskrift av resultat från varje funktionsanrop

def add(term1, term2):
    return term1 + term2

def subtract(term1, term2):
    return term1 - term2

def multiply(factor1, factor2):
    return factor1 * factor2

def divide(numerator, denominator):
    if denominator != 0:
        k = numerator/denominator
    else:
        k = 'INFINITE'
    return k

def mean(value1, value2):
    return (value1 + value2)/2

print("add(1, 3) =", add(1, 3))
print("add(7, 0) =", add(7, 0))
print("add(-2, 2) =", add(-2, 2))
print("add(-3, -5) =", add(-3, -5))

print("subtract(1, 3) =", subtract(1, 3))
print("subtract(7, 0) =", subtract(7, 0))
print("subtract(-2, 2) =", subtract(-2, 2))
print("subtract(-3, -5) =", subtract(-3, -5))

print("multiply(1, 3) =", multiply(1, 3))
print("multiply(7, 0) =", multiply(7, 0))
print("multiply(-2, 2) =", multiply(-2, 2))
print("multiply(-3, -5) =", multiply(-3, -5))

print("divide(1, 3) =", divide(1, 3))
print("divide(7, 0) =", divide(7, 0))
print("divide(-2, 2) =", divide(-2, 2))
print("divide(-3, -5) =", divide(-3, -5))

print("mean(1, 3) =", mean(1, 3))
print("mean(7, 0) =", mean(7, 0))
print("mean(-2, 2) =", mean(-2, 2))
print("mean(-3, -5) =", mean(-3, -5))

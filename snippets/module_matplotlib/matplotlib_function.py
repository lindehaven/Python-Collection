'''Plotta grafer med hjälp av modul'''

from matplotlib.pyplot import *

def f(x):
    '''Funktionsvärde x^3-2x'''
    return x**3 - 2*x # Eller x*x*x - 2*x

def d(x):
    '''Derivatavärde 3x^2-2'''
    return 3*x**2 - 2 # Eller 3*x*x - 2

xr = [] # kategorivärden
yf = [] # funktionsvärden
yd = [] # derivatavärden
for x in range(-10, 11): # x från -10 till 10
    xr.append(x) # fyll på kategorivärden
    yf.append(f(x)) # fyll på funktionsvärden
    yd.append(d(x)) # fyll på derivatavärden
scatter(xr, yf) # plotta funktionsvärden
scatter(xr, yd) # plott derivatavärden
show() # visa grafen

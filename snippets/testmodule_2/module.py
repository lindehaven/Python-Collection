'''Module v2

Denna modul använder funktioner i modulen statistics för att lösa uppgiften.

Funktionerna ska:
 a) returnera det lägsta av tre tal
 b) returnera det högsta av tre tal
 c) returnera medelvärdet av tre tal
 d) returnera medianen av tre tal
 e) returnera det lägsta av talen i en lista eller None om listan är tom
 f) returnera det högsta av talen i en lista eller None om listan är tom
 g) returnera medelvärdet av talen i en lista eller None om listan är tom
 h) returnera medianen av talen i en lista eller None om listan är tom
'''
from statistics import mean, median

def my_min(a, b, c):
    return min(a, b, c)

def my_max(a, b, c):
    return max(a, b, c)

def my_mean(a, b, c):
    return mean((a, b, c))

def my_median(a, b, c):
    return median((a, b, c))

def my_list_min(a):
    if a:
        return min(a)
    else:
        return None

def my_list_max(a):
    if a:
        return max(a)
    else:
        return None

def my_list_mean(a):
    if a:
        return mean(a)
    else:
        return None

def my_list_median(a):
    if a:
        return median(a)
    else:
        return None

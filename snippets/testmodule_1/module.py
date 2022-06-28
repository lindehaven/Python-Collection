'''Module v1

Denna modul löser uppgiften enbart med inbyggda funktioner d v s inga import.

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

def my_min(a, b, c): # Alternativ 1
    t = [a, b, c]
    t.sort()
    return t[0]

'''
def my_min(a, b, c): # Alternativ 2
    if a <= b <= c:
        return a
    elif b <= a <= c:
        return b
    else:
        return c
'''

def my_max(a, b, c): # Alternativ 1
    t = [a, b, c]
    t.sort(reverse=True)
    return t[0]

'''
def my_max(a, b, c): # Alternativ 2
    if a >= b >= c:
        return a
    elif b >= a >= c:
        return b
    else:
        return c
'''

def my_mean(a, b, c):
    return (a + b + c)/3

def my_median(a, b, c): # Alternativ 1
    t = [a, b, c]
    t.sort()
    return t[1]

'''
def my_median(a, b, c): # Alternativ 2
    if b <= a <= c or b >= a >= c:
        return a
    elif a <= b <= c or a >= b >= c:
        return b
    else:
        return c
'''

def my_list_min(a): # Alternativ 1
    if a:
        a.sort()
        return a[0]
    else:
        return None

'''
def my_list_min(a): # Alternativ 2
    if a:
        m = a[0]
        for e in a:
            if e < m:
                m = e
        return m
    else:
        return None
'''

def my_list_max(a): # Alternativ 1
    if a:
        a.sort(reverse=True)
        return a[0]
    else:
        return None

'''
def my_list_max(a): # Alternativ 2
    if a:
        a.sort()
        return a[-1]
    else:
        return None
'''

'''
def my_list_max(a): # Alternativ 3
    if a:
        m = a[0]
        for e in a:
            if e > m:
                m = e
        return m
    else:
        return None
'''

def my_list_mean(a):
    if a:
        return sum(a) / len(a)
    else:
        return None

def my_list_median(a):
    if a:
        a.sort()
        i = len(a) // 2
        if len(a) % 2 == 1:
            return a[i]
        else:
            return (a[i-1] + a[i]) / 2
    else:
        return None

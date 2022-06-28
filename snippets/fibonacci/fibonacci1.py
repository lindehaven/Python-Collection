'''fibonacci1

Visar ett klassiskt exempel på rekursion i Python.
Beräknar Fibonacci-serie.
'''

def fibonacci(n):
    '''Rekursiv funktion för beräkning av fibonacci-serie'''
    if n <= 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    for i in range(1, 10):
        print(i, ':', fibonacci(i))

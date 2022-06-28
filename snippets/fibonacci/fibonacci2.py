'''fibonacci2

Beräknar Fibonacci-serie utan rekursion.
'''

def fibonacci(n):
    '''Funktion för beräkning av fibonacci-serie'''
    f = [1, 2]
    if n > 0:
        for i in range(2, n+1):
            f.append(f[i-2] + f[i-1])
        return f[n-1]
    else:
        return 0

if __name__ == '__main__':
    for i in range(1, 10):
        print(i, ':', fibonacci(i))

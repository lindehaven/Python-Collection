def recursive_factorial(n):
    return 1 if n < 1 else n * recursive_factorial(n-1)

def for_factorial(n):
    r = 1 if n < 1 else n
    for i in range(n-1, 1, -1):
        r *= i
    return r

def while_factorial(n):
    r = 1 if n < 1 else n
    while n > 1:
        n -= 1
        r *= n
    return r

if __name__ == '__main__':
    print(recursive_factorial(5))
    print(for_factorial(5))
    print(while_factorial(5))

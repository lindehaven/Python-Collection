'''fibonacci1'''

def fibonacci(n):
    '''Recursively calculates the n:th number in the Fibonacci series.
    
    Returns
        a(n)=0 , n=1.
        a(n)=1 , n=2.
        a(n)=a(n−1)+a(n−2) , n>2.
    '''
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    for i in range(1, 10):
        print(i, ':', fibonacci(i))

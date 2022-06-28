'''fibonacci2'''

def fibonacci(n):
    '''Calculates the n:th number in the Fibonacci series.
    
    Returns
        a(n)=0 , n=1.
        a(n)=1 , n=2.
        a(n)=a(n−1)+a(n−2) , n>2.
    '''
    f = [0, 1]
    if n > 0:
        for i in range(2, n+1):
            f.append(f[i-2] + f[i-1])
        return f[n-1]
    else:
        return 0

if __name__ == '__main__':
    for i in range(1, 10):
        print(i, ':', fibonacci(i))

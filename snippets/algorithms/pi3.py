# Wallis product
def pi(x=10):
    p = 1.0
    for n in range(1, x+1):
        n2 = 4*(n**2)
        p = p*n2/(n2-1)
    return 2*p

print(pi(10_000_000))

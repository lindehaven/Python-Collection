# From p.53 in "The Joy of Pi". sin(pi/6) = 1/2
# 3 + 3*(1/24) + 3*(1/24)*(9/80) + 3*(1/24)*(9/80)*(25/168)
# The numerators 1, 9, 25, ... are given by (2x + 1) ^ 2
# The denominators 24, 80, 168 are given by 16x^2 +40x + 24

def pi(places=11):
    extra = 8
    one = 10 ** (places+extra)
    t, c, n, na, d, da = 3*one, 3*one, 1, 0, 0, 24
    while t > 1:
        n, na, d, da = n+na, na+8, d+da, da+32
        t = t * n // d
        c += t
    ps = str(c // (10 ** extra))
    return ps[0]+'.'+ps[1:]

print(pi())

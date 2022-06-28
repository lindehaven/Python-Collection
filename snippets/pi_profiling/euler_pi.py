import math

def euler_pi(d):
    q = 1
    e = 0
    t = round(math.pi**2 / 6, d) - 10**-d / 12
    while e < t:
        e += 1 / q**2
        q += 1
    return math.sqrt(6 * e)

if __name__ == '__main__':
    print(euler_pi(6))
    print(math.pi)

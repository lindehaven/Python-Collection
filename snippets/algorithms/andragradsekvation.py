from cmath import sqrt

a = int(input("Koefficient a? "))
b = int(input("Koefficient b? "))
c = int(input("Konstant c? "))

r = -b/(2*a)
s = (b**2-4*a*c)/(2*a)

##if s == 0:
##    print("x1 =", r)
##    print("x2 =", r)
##else:
print("x1 =", r + sqrt(s))
print("x2 =", r - sqrt(s))

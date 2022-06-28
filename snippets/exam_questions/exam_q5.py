a = int(input())
if a > 3:
    if a <= 2:
        b = 2
    else:
        b = 3
elif a < 3:
    b = 3
else:
    b = a
a = b
print(a)

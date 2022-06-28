'''Equal after n iterations'''
a = 10.0
b = 20.0
n = 1
while a < 35.0:
    if a == b:
        print(f'n={n}: a={a} b={b}')
    n += 1
    a += 0.5
    b += 0.1

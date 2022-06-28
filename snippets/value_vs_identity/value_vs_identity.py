a = [1,2,3]
b = [1,2,3]
c = b

if a == b:
    print("a and b have the same value.")
if a is b:
    print("a and b are the same list.")

if a == c:
    print("a and c have the same value.")
if b is c:
    print("b and c are the same list.")

if b == c:
    print("b and c have the same value.")
if a is c:
    print("a and c are the same list.")

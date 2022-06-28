# 1. Which of the following numbers are valid Python integers?
# 110, 1.0, 17.5, -39, -2.3
assert isinstance(110, int) == True
assert isinstance(1.0, int) == False
assert isinstance(17.5, int) == False
assert isinstance(-39, int) == True
assert isinstance(-2.3, int) == False

# 2. What are the results of the following operations and explain why:
assert 15 + 20 * 3 == 75
assert 13 // 2 + 3 == 9
assert 31 + 10 // 3 == 34
assert 20 % 7 // 3 == 2
assert 2 ** 3 ** 2 == 2 ** (3 ** 2) == 2 ** 9 == 512
assert 2 ** 2 ** 3 == 2 ** (2 ** 3) == 2 ** 8 == 256


# 3. What happens when you evaluate 1 // 0 in the Python console?
# Why does this happen?
# Traceback (most recent call last):
#   File "<pyshell#0>", line 1, in <module>
#     1//0
# ZeroDivisionError: integer division or modulo by zero
try:
    a = 1//0
except ZeroDivisionError as e:
    assert str(e) == 'integer division or modulo by zero'

print('All tests passed OK.')

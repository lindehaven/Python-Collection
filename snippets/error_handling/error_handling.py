import math

def divide_offensive(numerator, denominator):
    if denominator is not 0:
        return numerator / denominator
    else:
        assert False, math.nan

def divide_defensive(numerator, denominator):
    if denominator is not 0 and isinstance(denominator, (int, float)):
        return numerator / denominator
    else:
        return math.nan

def divide_exception(numerator, denominator):
    try:
        return numerator / denominator
    except (ZeroDivisionError, TypeError):
        return math.nan

print(divide_offensive(2.3, 2))
print(divide_offensive(2.3, 0))
print(divide_offensive(2.3, '2'))

print(divide_defensive(2.3, 2))
print(divide_defensive(2.3, 0))
print(divide_defensive(2.3, 'a'))
print(divide_defensive(2.3, [2]))

print(divide_exception(2.3, 2))
print(divide_exception(2.3, 0))
print(divide_exception(2.3, 'a'))
print(divide_exception(2.3, [2]))

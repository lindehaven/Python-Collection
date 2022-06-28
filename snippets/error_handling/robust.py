import math

def divide_exception(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return math.nan

def divide_defensive(numerator, denominator):
    if denominator is not 0:
        return numerator / denominator
    else:
        return math.nan

def divide_offensive(numerator, denominator):
    if denominator is not 0:
        return numerator / denominator
    else:
        assert False, math.nan

print(divide_exception(1, 0))
print(divide_defensive(1, 0))
print(divide_offensive(1, 0))

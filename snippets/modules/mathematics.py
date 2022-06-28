'''Mathematics

Provides functions for addition, subtraction, multiplication and division.
'''

def add(term1, term2):
    '''Adds'''
    return term1 + term2

def sub(term1, term2):
    '''Subtracts'''
    return term1 - term2

def mul(factor1, factor2):
    '''Multiplies'''
    return factor1 * factor2

def div(numerator, denominator):
    '''Divides'''
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return None

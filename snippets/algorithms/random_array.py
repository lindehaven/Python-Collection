'''Random array'''

from random import randint

def get_random_array(elements=10, min_value=1, max_value=100):
    '''Fills an array with random integers and returns the array'''
    arr = []
    for _ in range(elements):
        arr.append(randint(min_value, max_value))
    return arr

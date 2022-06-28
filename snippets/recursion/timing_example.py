from random import randint, sample
from time import perf_counter

ELEMENTS = 10_000
ELEMENT_MIN = 0
ELEMENT_MAX = 1_000_000
SEARCH_MIN = 0
SEARCH_MAX = 10_000

def binary_search(number, array, lo, hi):
    if hi < lo:
        return -1 # no more numbers
    mid = (lo + hi) // 2
    if number == array[mid]:
        return mid # found
    elif number < array[mid]:
        return binary_search(number, array, lo, mid - 1)
    else:
        return binary_search(number, array, mid + 1, hi)

if __name__ == '__main__':
    anum = randint(SEARCH_MIN, SEARCH_MAX)
    array = sample(list(range(ELEMENT_MIN, ELEMENT_MAX)), ELEMENTS)
    array = sorted(array)
    t0 = perf_counter()
    pos = binary_search(anum, array, 0, len(array) - 1)
    t1 = perf_counter()
    if pos < 0:
        print(anum, 'was not found')
    else:
        print(anum, 'was found at position', pos)
    print(ELEMENTS, 'elements took', t1-t0, 'seconds')

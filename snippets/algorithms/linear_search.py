'''Linear search - assignment 1-2 on page 36'''

from time import perf_counter
from random_array import get_random_array

ELEMENTS = 30_000 # number of elements in the array
MIN_VALUE = 1 # minimum value for an element in the array
MAX_VALUE = 100 # maximum value for an element in the array

def linear_search(number, array):
    '''Performs linear search for a number in an array and returns position'''
    for index in range(len(array)):
        if number == array[index]:
            return index
    return -1

def main():
    '''Main function'''
    array = get_random_array(ELEMENTS, MIN_VALUE, MAX_VALUE)
    anum = int(input('Vilket tal vill du söka efter? '))
    time_0 = perf_counter()
    pos = linear_search(anum, array)
    time_1 = perf_counter()
    print('Sökte talet', anum, 'i listan', array)
    if pos < 0:
        print('Talet', anum, 'finns inte i listan')
    else:
        print('Talet', anum, 'hittades på plats', pos+1)
    print('Sökning i', ELEMENTS, 'element tog', time_1 - time_0, 's.')

if __name__ == '__main__':
    main()

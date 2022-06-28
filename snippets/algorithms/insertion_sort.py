'''Insertion Sort'''

from random_array import get_random_array

ELEMENTS = 20 # number of elements in the array
MIN_VALUE = 1 # minimum value for an element in the array
MAX_VALUE = 100 # maximum value for an element in the array

def insertion_sort(array):
    '''Performs insertion sort of an array'''
    for outer in range(1, len(array)):
        value = array[outer]
        inner = outer
        while inner > 0 and array[inner-1] > value:
            array[inner] = array[inner-1]
            inner = inner-1
        array[inner] = value

def main():
    '''Main function'''
    array = get_random_array(ELEMENTS, MIN_VALUE, MAX_VALUE)
    print('Osorterade listan:', array)
    insertion_sort(array)
    print('Sorterade listan:', array)

if __name__ == '__main__':
    main()

'''Bubble Sort'''

from random_array import get_random_array

ELEMENTS = 20 # number of elements in the array
MIN_VALUE = 1 # minimum value for an element in the array
MAX_VALUE = 100 # maximum value for an element in the array

def bubble_sort(array):
    '''Performs bubble sort of an array'''
    for outer in range(len(array)-1, 0, -1):
        for inner in range(outer):
            if array[inner] > array[inner+1]:
                array[inner], array[inner+1] = array[inner+1], array[inner]

def main():
    '''Main function'''
    array = get_random_array(ELEMENTS, MIN_VALUE, MAX_VALUE)
    print('Osorterade listan:', array)
    bubble_sort(array)
    print('Sorterade listan:', array)

if __name__ == '__main__':
    main()

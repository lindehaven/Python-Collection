'''Quicksort'''

from random_array import get_random_array

ELEMENTS = 20 # number of elements in the array
MIN_VALUE = 1 # minimum value for an element in the array
MAX_VALUE = 100 # maximum value for an element in the array

def quick_sort(array):
    '''Makes quicksort of an array more convenient'''
    quick_sort_splitter(array, 0, len(array)-1)

def quick_sort_splitter(array, first, last):
    '''Splits the array and performs quicksort of each partition'''
    if first < last:
        splitpoint = partition(array, first, last)
        quick_sort_splitter(array, first, splitpoint-1)
        quick_sort_splitter(array, splitpoint+1, last)

def partition(array, first, last):
    '''Partitions the array and returns splitpoint'''
    pivot = array[first]
    lo_mark = first+1
    hi_mark = last
    done = False
    while not done:
        while lo_mark <= hi_mark and array[lo_mark] <= pivot:
            lo_mark = lo_mark + 1
        while array[hi_mark] >= pivot and hi_mark >= lo_mark:
            hi_mark = hi_mark -1
        if hi_mark < lo_mark:
            done = True
        else:
            array[lo_mark], array[hi_mark] = array[hi_mark], array[lo_mark]
    array[first], array[hi_mark] = array[hi_mark], array[first]
    return hi_mark

def main():
    '''Main function'''
    array = get_random_array(ELEMENTS, MIN_VALUE, MAX_VALUE)
    print('Osorterade listan:', array)
    quick_sort(array)
    print('Sorterade listan:', array)

if __name__ == '__main__':
    main()

'''Binary search - assignment 5 on page 37'''

from random import randint

ELEMENTS = 20 # number of elements in the array
MIN_VALUE = 1 # minimum value for an element in the array
MAX_VALUE = 100 # maximum value for an element in the array

def get_random_sorted_array(elements, min_value, max_value):
    '''Fills an array with random integers and returns the sorted array'''
    arr = []
    for _ in range(elements):
        arr.append(randint(min_value, max_value))
    return sorted(arr)

def binary_search(number, array):
    '''Performs binary search for a number in an array'''
    lower = 0
    upper = len(array) - 1
    found = False
    while lower <= upper and not found:
        mid = (lower + upper) // 2
        if number == array[mid]:
            found = True
        else:
            if number < array[mid]:
                upper = mid - 1 # search lower half
            else:
                lower = mid + 1 # search upper half
    if found:
        return mid # found
    else:
        return -1 # not found

def main():
    '''Main function'''
    array = get_random_sorted_array(ELEMENTS, MIN_VALUE, MAX_VALUE)
    print('Listan =', array)
    a_number = int(input('Vilket tal vill du söka efter? '))
    pos = binary_search(a_number, array)
    if pos < 0:
        print('Talet', a_number, 'finns inte i listan')
    else:
        print('Talet', a_number, 'hittades på plats', pos)

if __name__ == '__main__':
    main()

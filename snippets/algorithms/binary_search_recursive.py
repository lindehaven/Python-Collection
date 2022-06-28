'''Binary search recursive - assignment 5 on page 37'''

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

def binary_search(number, array, lower, upper):
    '''Performs recursive binary search for a number in an array'''
    if upper < lower:
        return -1 # not found
    mid = (lower + upper) // 2
    if number == array[mid]:
        return mid # found
    elif number < array[mid]:
        return binary_search(number, array, lower, mid - 1) # search lower half
    else:
        return binary_search(number, array, mid + 1, upper) # search upper half

def main():
    '''Main function'''
    array = get_random_sorted_array(ELEMENTS, MIN_VALUE, MAX_VALUE)
    print('Listan =', array)
    a_number = int(input('Vilket tal vill du söka efter? '))
    pos = binary_search(a_number, array, 0, len(array) - 1)
    if pos < 0:
        print('Talet', a_number, 'finns inte i listan')
    else:
        print('Talet', a_number, 'hittades på plats', pos)

if __name__ == '__main__':
    main()

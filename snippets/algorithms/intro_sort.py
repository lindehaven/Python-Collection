'''Introsort

Introsort or introspective sort is a hybrid sorting algorithm that provides both
fast average performance and (asymptotically) optimal worst-case performance. It
begins with quicksort, it switches to heapsort when the recursion depth exceeds
a level based on (the logarithm of) the number of elements being sorted and it
switches to insertionsort when the number of elements is below some threshold.
This combines the good parts of the three algorithms, with practical performance
comparable to quicksort on typical data sets and worst-case O(n log n) runtime
due to the heap sort. Since the three algorithms it uses are comparison sorts,
it is also a comparison sort.
'''

import math
from heapq import heappush, heappop
from random_array import get_random_array

def heapsort():
    '''Sort array using heapsort algorithm'''
    global arr
    h = []
    for value in arr:
        heappush(h, value)
    arr = []
    arr = arr + [heappop(h) for i in range(len(h))]

def insertionsort(begin, end):
    '''Sort array using insertion sort algorithm'''
    left = begin
    right = end
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

def partition(low, high):
    '''This function takes last element as pivot, places the pivot element at
    its correct position in sorted array, and places all smaller (smaller than
    pivot) to left of pivot and all greater elements to right of pivot'''
    global arr
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1

def median_of_three(a, b, d):
    '''Finds the median of the three elements in array with index a, b, d'''
    global arr
    A = arr[a]
    B = arr[b]
    C = arr[d]
    if A <= B and B <= C or C <= B and B <= A:
        return b
    elif B <= A and A <= C or C <= A and A <= B:
        return a
    else:
        return d

def introsort_util(begin, end, depth_limit):
    '''Implements introsort'''
    global arr
    size = end - begin
    if size < 16:
        insertionsort(begin, end)
        return
    if depth_limit == 0:
        heapsort()
        return
    pivot = median_of_three(begin, begin + size // 2, end)
    (arr[pivot], arr[end]) = (arr[end], arr[pivot])
    partition_point = partition(begin, end)
    introsort_util(begin, partition_point - 1, depth_limit - 1)
    introsort_util(partition_point + 1, end, depth_limit - 1)

def introsort(begin, end):
    '''Initialises the depth_limit as 2 * log(length(data))'''
    depth_limit = 2 * math.log2(end - begin)
    introsort_util(begin, end, depth_limit)

def main():
    '''Main function'''
    global arr
    ELEMENTS = 1_000 # number of elements in the array
    MIN_VALUE = 1 # minimum value for an element in the array
    MAX_VALUE = 10_000 # maximum value for an element in the array
    arr = get_random_array(ELEMENTS, MIN_VALUE, MAX_VALUE)
    print('Osorterade listan:', arr)
    introsort(0, ELEMENTS-1)
    print('Sorterade listan:', arr)

arr = []
if __name__ == '__main__':
    main()

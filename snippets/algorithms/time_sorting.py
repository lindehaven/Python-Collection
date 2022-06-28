'''Times the execution of different sorting algorithms'''

from time import perf_counter
from random_array import get_random_array
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort

ELEMENTS = 5_000 # number of elements in the array
MIN_VALUE = 1 # minimum value for an element in the array
MAX_VALUE = 100 # maximum value for an element in the array

array = get_random_array(ELEMENTS, MIN_VALUE, MAX_VALUE)
array1 = array.copy()
array2 = array.copy()
array3 = array.copy()
print("Sorting", ELEMENTS, "elements, please wait ...")
t0 = perf_counter()
bubble_sort(array1)
print("Bubble sort took    :", perf_counter()-t0, "seconds.")
t0 = perf_counter()
insertion_sort(array2)
print("Insertion sort took :", perf_counter()-t0, "seconds.")
t0 = perf_counter()
quick_sort(array3)
print("Quick sort took     :", perf_counter()-t0, "seconds.")

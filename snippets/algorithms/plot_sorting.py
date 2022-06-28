'''Times and plots the execution of different sorting algorithms'''

import sys
from matplotlib.pyplot import *
from time import perf_counter
from random_array import get_random_array
from intro_sort import introsort
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort
import intro_sort as isort

MAX = 5_000
INC = 50

print('Sorting', MAX, 'elements, please wait...', flush=True)
sys.setrecursionlimit(MAX)
n = INC
x = []

# Let each be an empty list to measure it
y1 = 0  # Bubble Sort
y2 = 0 # Insertion Sort
y3 = 0 # Quick Sort
y0 = [] # Intro Sort
y4 = [] # Python Sort
unsorted = get_random_array(MAX, 0, MAX)

while n <= MAX:

    x.append(n)
    isort.arr = unsorted[:n]

    if isinstance(y1, list):
        array1 = isort.arr.copy()
        t0 = perf_counter()
        bubble_sort(array1)
        y1.append(perf_counter()-t0)

    if isinstance(y2, list):
        array2 = isort.arr.copy()
        t0 = perf_counter()
        insertion_sort(array2)
        y2.append(perf_counter()-t0)

    if isinstance(y3, list):
        array3 = isort.arr.copy()
        t0 = perf_counter()
        quick_sort(array3)
        y3.append(perf_counter()-t0)

    if isinstance(y0, list):
        t0 = perf_counter()
        introsort(0, n-1)
        y0.append(perf_counter()-t0)

    if isinstance(y4, list):
        array4 = isort.arr.copy()
        t0 = perf_counter()
        array4.sort()
        y4.append(perf_counter()-t0)

    n += INC

if y1: plot(x, y1, linewidth=1.0, label='Bubble Sort')
if y2: plot(x, y2, linewidth=1.0, label='Insertion Sort')
if y3: plot(x, y3, linewidth=1.0, label='Quick Sort')
if y0: plot(x, y0, linewidth=1.0, label='Intro Sort')
if y4: plot(x, y4, linewidth=1.0, label='Python Sort')

xlabel('Number of elements')
ylabel('Execution Time (s)')
title('Sorting Algorithms')
legend()
show()

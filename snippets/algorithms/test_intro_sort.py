from random_array import get_random_array
from intro_sort import introsort
import intro_sort as isort

isort.arr = get_random_array(100, -10, 10)
s_arr = isort.arr.copy()
introsort(0, 99)
s_arr.sort()
assert isort.arr == s_arr

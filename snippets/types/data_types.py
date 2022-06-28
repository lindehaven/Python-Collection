str_var = "This is a string consisting of more than 20 characters"
print(str_var)
print(str_var[-3:])
print(str_var[3:11])
print(str_var[:2])

list_var = [-2, 3, 0, -7, 8]
print(list_var)
print(list_var[0] - list_var[1])
print(list_var[1] + list_var[2] + list_var[4])
list_var[0] = list_var[0] * list_var[1]
print(list_var)

tuple_var = (-2.7, 3.3)
print(tuple_var)
avg = (tuple_var[0] + tuple_var[1]) / 2
print(avg)
print("%.3f" % avg)
tuple_var = tuple_var[1], tuple_var[0]
print(tuple_var)

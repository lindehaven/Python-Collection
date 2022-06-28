# Dictionary
legs_dict = {'Fish':100, 'Human':2, 'Tripod':3}

# Dictionary items
print(legs_dict.items())

# Dictionary keys
print(legs_dict.keys())

# Dictionary values
print(legs_dict.values())

# i) List comprehension
legs_list = [(being, legs) for being, legs in legs_dict.items()]
print(legs_list)
# ii) List from dictionary items
print(list(legs_dict.items()))

# Copy list
legs_list_i = legs_list.copy()
legs_list_ii = legs_list.copy()

# i) Sort with callback function
def compare(x):
    return x[1]
legs_list_i.sort(key=compare)
print(legs_list_i)
# ii) Sort with lambda
legs_list_ii.sort(key=lambda x : x[1])
print(legs_list_ii)

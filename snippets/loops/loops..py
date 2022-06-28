# range() is a simple way to create an iterable.
# Loops from 23 to 99 in steps of 20
for iteration in range(23, 100, 20):
    print(iteration/10)

# A string is an iterable.
# Loops through each character in the string.
for character in "Hej du glade":
    print(character, end="")
print()

# A list is an iterable.
# Loops through each value in the list.
for value in [0, 1, 1, 2, 3, 5, 8, 13, 21]:
    print(value)

# A tuple is an iterable.
# Loops through each value in the tuple.
for value in (0, 1, 1, 2, 3, 5, 8, 13, 21):
    print(value)


# Nestled loops.
# Function that finds a three-dimensional coordinate.
def find_coord(inx, iny, inz):
    found = False
    for x in range(1, 11): # Outer loop
        for y in range(1, 11): # Inner loop
            for z in range(1, 11): # Inner-most loop
                if x==inx and y==iny and z==inz:
                    found = True
    return found

print(find_coord(2, 3, 4))
print(find_coord(5, 7, 1))
print(find_coord(5, 7, 11))


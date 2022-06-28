print()
print("for loop", end="\t")
for iteration in range(5):
    if iteration != 1:
        print(iteration, end=" ")
    else:
        break

print()
print("while loop", end="\t")
iteration = 0
while iteration < 5:
    if iteration != 1:
        print(iteration, end=" ")
    else:
        break
    iteration += 1


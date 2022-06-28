print()
print("for loop", end="\t")
for iteration in range(5):
    if iteration != 3:
        print(iteration, end=" ")
    else:
        continue

print()
print("while loop", end="\t")
iteration = 0
while iteration < 5:
    if iteration != 3:
        print(iteration, end=" ")
    else:
        iteration += 1
        continue
    iteration += 1


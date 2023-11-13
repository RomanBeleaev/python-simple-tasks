print("\n")

for y in range(1, 11):
    for x in range(1, 11):
        if y == 1 or y == 10 or x == 1 or x == 10:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()

print("\n")
size = int(input("Enter the size of the pattern:"))
x = 0

while x < size:
    y = 0
    while y < size:
        print("*", end=" ")
        y += 1
    print()
    x += 1
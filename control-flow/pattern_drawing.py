#assign & compute variables
postive_integer = int(input("Enter the size of the pattern: "))

row = 0
while row < postive_integer:
    for _ in range(postive_integer):
        print("*", end="")
    print()
    row += 1
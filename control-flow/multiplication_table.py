#assign & compute variables
number = int(input("Enter a number to see its multiplication table: "))

for currentnumber in range(1, 11):
    product = number * currentnumber
    print(f"{number} * {currentnumber} = {product}")
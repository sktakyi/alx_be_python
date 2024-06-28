#assign compute variables
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# compute the calculation using match-case
match operation:
    case "+":
        operation = num1 + num2
        print(f"The result is {operation}")
    case "-":
        operation = num1 - num2
        print(f"The result is {operation}")
    case "*":
        operation = num1 * num2
        print(f"The result is {operation}")
    case "/":
        if num2 != 0:
            operation = num1 / num2
            print(f"The result is {operation}")
        else:
            print("Cannot divide by zero.")
#assign & compute variables
def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
                if num2 == 0:
                      return "Error:Division by zero"
                elif num1 ==0:
                     return "Can not divide by zero"
                else:
                     return num1 / num2
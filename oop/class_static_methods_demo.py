class Calculator:
    calculation_type = "Calculation type: Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(cls.calculation_type)
        return a * b

# Testing the Calculator class
def main():
    # Test the static method
    result_add = Calculator.add(5, 3)
    print(f"The sum of 5 and 3 is: {result_add}")

    # Test the class method
    result_multiply = Calculator.multiply(5, 3)
    print(f"The product of 5 and 3 is: {result_multiply}")
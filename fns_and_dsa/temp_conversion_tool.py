FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

# Main function for user interaction
def main():
    try:
        temperature = float(input("Enter the temperature to convert:"))
        degree = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()
        
        if degree == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temperature}°F")
        elif degree == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temperature}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Invalid temperature. Please enter a numeric value. {e}")


if __name__ == "__main__":
     main()
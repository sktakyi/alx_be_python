from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the formatted date and time
    print(f"Current date and time: {formatted_datetime}")
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    # Get the current date
    current_date = datetime.now()
    # Calculate future date
    future_date = current_date + timedelta(days=days)
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Print the future date
    print(f"Future date after {days} days: {formatted_future_date}")
    return future_date

def main():
    # Part 1: Call date and time
    current_date = display_current_datetime()
    # Part 2: Call future date
    future_date = calculate_future_date()
    # Return useful values if needed
    return current_date, future_date

if __name__ == "__main__":
    main()
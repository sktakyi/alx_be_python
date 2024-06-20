# Get user input
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Compute and output monthly savings results
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are ${monthly_savings}.")

# Compute and output projected annual savings
annual_savings_projection = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${annual_savings_projection}.")

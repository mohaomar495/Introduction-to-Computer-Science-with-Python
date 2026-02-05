# Author: Mohamed Adde
# Date: Tue Feb 03 2026

annual_salary = float(input("Enter your annual salary: "))

# Cost of dream home
total_cost = 1000000

# Semi-annual raise
semi_annual_raise = 0.07  # (7%)

# Portion of the cost needed for a down payment
portion_down_payment = 0.25  # (25%)

annual_return = 0.04  # annual return rate of (4%)
months = 36

down_payment = total_cost * portion_down_payment

# Bisection search bounds (0-10000 represents 0.0 to 1.0)
low = 0
high = 10000
steps = 0
best_rate = 0.0

while low <= high:
    steps += 1
    guess = (low + high) // 2
    portion_saved = guess / 10000

    current_savings = 0.0
    current_salary = annual_salary
    monthly_salary = current_salary / 12

    for month in range(1, months + 1):
        current_savings += current_savings * (annual_return / 12)
        current_savings += monthly_salary * portion_saved

        if month % 6 == 0:
            current_salary += current_salary * semi_annual_raise
            monthly_salary = current_salary / 12

    if abs(current_savings - down_payment) <= 100:
        best_rate = portion_saved
        break
    elif current_savings < down_payment:
        low = guess + 1
    else:
        high = guess - 1

if best_rate is None:
    print("It is not possible to pay the down payment in three years.")
else:
    print(f"Best savings rate: {best_rate}")
    print(f"Steps in bisection search: {steps}")

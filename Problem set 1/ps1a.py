# Author: Mohamed Adde
# Date: Tue Feb 03 2026

annual_salary = float(input("Enter your annual salary: "))

# Saving for down payment
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

# Cost of dream home
total_cost = float(input("Enter the cost of your dream home: "))

# Portion of the cost needed for a down payment
portion_down_payment = 0.25  # (25%)

#  The Amount that you have saved thus far.
current_savings = 0

annual_return = 0.04  # return rate of (4%)
monthly_salary = annual_salary / 12
months = 0

down_payment = total_cost * portion_down_payment

while current_savings < down_payment:
    current_savings += current_savings * (annual_return / 12)
    current_savings += monthly_salary * portion_saved
    months += 1

print(f"Number of months: {months}")

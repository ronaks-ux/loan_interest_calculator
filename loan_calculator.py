## loan_calculator.py


```python
import math


print("Loan EMI Calculator")


principal = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan tenure (years): "))


monthly_rate = annual_rate / (12 * 100)
months = years * 12


emi = (principal * monthly_rate * math.pow(1 + monthly_rate, months)) / (math.pow(1 + monthly_rate, months) - 1)


total_payment = emi * months
interest_paid = total_payment - principal


print(f"\nMonthly EMI: {emi:.2f}")
print(f"Total Payment: {total_payment:.2f}")
print(f"Total Interest Paid: {interest_paid:.2f}")

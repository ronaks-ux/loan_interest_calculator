---

## loan_calculator.py

```python
import math

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

print("Loan EMI Calculator")

while True:
    principal = get_float("Enter loan amount: ")
    annual_rate = get_float("Enter annual interest rate (%): ")
    years = get_float("Enter loan tenure (years): ")

    monthly_rate = annual_rate / (12 * 100)
    months = int(years * 12)

    emi = (principal * monthly_rate * math.pow(1 + monthly_rate, months)) / (math.pow(1 + monthly_rate, months) - 1)
    total_payment = emi * months
    interest_paid = total_payment - principal

    print(f"\nMonthly EMI: {emi:.2f}")
    print(f"Total Payment: {total_payment:.2f}")
    print(f"Total Interest Paid: {interest_paid:.2f}")

    # EMI schedule (optional)
    print("\nEMI Schedule:")
    remaining = principal
    for month in range(1, months + 1):
        interest = remaining * monthly_rate
        principal_payment = emi - interest
        remaining -= principal_payment
        print(f"Month {month}: EMI={emi:.2f}, Principal={principal_payment:.2f}, Interest={interest:.2f}, Remaining={remaining:.2f}")

    cont = input("\nDo you want to calculate another loan? (y/n): ").lower()
    if cont != 'y':
        break
```

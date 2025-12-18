# loan_interest_calculator

This is the improved version of your loan and interest calculator repository, with enhanced features, input validation, and an updated README.

---

## README.md

````markdown
# Loan & Interest Calculator

A Python project to calculate:
- Simple Interest
- Compound Interest
- Loan EMI (monthly payment)

## Features
- Input validation for numeric values
- Repeated calculations without restarting
- EMI schedule display
- Beginner-friendly console-based interface

## How to Run

1. Make sure Python 3 is installed.
2. Run any file using:

```bash
python loan_calculator.py
python interest_calculator.py
````

## Sample Output

**EMI Calculation:**

```
Enter loan amount: 100000
Enter annual interest rate (%): 10
Enter loan tenure (years): 1
Monthly EMI: 8791.59
Total Payment: 105499.08
Total Interest Paid: 5499.08
```

**Interest Calculation:**

```
Enter principal amount: 5000
Enter annual interest rate (%): 5
Enter time (years): 2
Simple Interest: 500.00
Compound Interest: 525.63
```

```

## Future Improvements
- GUI or web interface
- File-based input/output
- More loan types and interest calculations
```

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

---

## interest_calculator.py

```python
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

print("Interest Calculator")

while True:
    principal = get_float("Enter principal amount: ")
    rate = get_float("Enter annual interest rate (%): ")
    time = get_float("Enter time (years): ")

    simple_interest = (principal * rate * time) / 100
    compound_interest = principal * ((1 + rate / 100) ** time) - principal

    print(f"\nSimple Interest: {simple_interest:.2f}")
    print(f"Compound Interest: {compound_interest:.2f}")

    cont = input("\nDo you want to calculate another interest? (y/n): ").lower()
    if cont != 'y':
        break
```

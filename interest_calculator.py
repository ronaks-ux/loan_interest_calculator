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

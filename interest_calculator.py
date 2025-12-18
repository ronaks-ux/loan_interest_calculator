print("Interest Calculator")


principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time (years): "))


simple_interest = (principal * rate * time) / 100
compound_interest = principal * ((1 + rate / 100) ** time) - principal


print(f"\nSimple Interest: {simple_interest:.2f}")
print(f"Compound Interest: {compound_interest:.2f}")

#Day 9 of learning Python...

budget = float(input("Enter Monthly Budget:"))
spent = float(input("Enter Total Spent:"))

balance = budget - spent

if balance < 0:
    print(f"!! ALERT: You are Over-Budget by {abs(balance)}")
    # abs(balance) → converts negative to positive for clean display (e.g. -500 → 500)
else:
    print(f">> SAFE: You still have {balance} left")

print("\nSmart Money, Smart Life. Learn with me.")
monthly_budget = float(input("Enter your monthly budget: "))

rent = float(input("Enter rent cost: "))
food = float(input("Enter food cost: "))
gas = float(input("Enter gas cost: "))

total_spent = rent + food + gas
remaining = monthly_budget - total_spent

print("\n----- Budget Summary -----")
print("Monthly Budget:", monthly_budget)
print("Total Spent:", total_spent)
print("Remaining:", remaining)
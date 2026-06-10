monthly_budget = float(input("Enter your monthly budget: "))

total_spent = 0

while True:
    
    expense = input("\nEnter expense amount (or type 'done'): ")

    if expense.lower() == "done":
        break

    total_spent = total_spent + float(expense)

remaining = monthly_budget - total_spent

print("\n----- Budget Summary -----")
print("Total Spent:", total_spent)
print("Remaining Budget:", remaining)

if remaining < 0:
    print("WARNING: You are over budget!")
    
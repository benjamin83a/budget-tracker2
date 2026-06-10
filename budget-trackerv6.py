monthly_budget = float(input("Enter your monthly budget: "))

expenses = {}

while True:

    category = input("\nEnter category (or type 'done'): ")

    if category.lower() == "done":
        break

    amount = float(input("Enter amount: "))

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

total_spent = sum(expenses.values())
remaining = monthly_budget - total_spent

print("\n----- Budget Summary -----")

for category, amount in expenses.items():
    print(category + ":", amount)

print("\nTotal Spent:", total_spent)
print("Remaining Budget:", remaining)

if remaining < 0:
    print("WARNING: You are over budget!")

# Save to CSV

file = open("expenses.csv", "w")

file.write("Category,Amount\n")

for category, amount in expenses.items():
    file.write(f"{category},{amount}\n")

file.close()

print("\nCSV file saved.")
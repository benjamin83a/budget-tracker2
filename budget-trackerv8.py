import matplotlib.pyplot as plt

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

    percentage = (amount / total_spent) * 100
    bar_length = int(percentage / 5)
    bar = "█" * bar_length

    print(f"{category}: ${amount:.2f} ({percentage:.1f}%) {bar}")

print("\nTotal Spent:", f"${total_spent:.2f}")
print("Remaining Budget:", f"${remaining:.2f}")

if remaining < 0:
    print("WARNING: You are over budget!")

categories = list(expenses.keys())
amounts = list(expenses.values())

plt.pie(amounts, labels=categories, autopct="%1.1f%%")

plt.title("Monthly Spending Breakdown")

plt.show()


# Save to CSV

file = open("expenses.csv", "w")

file.write("Category,Amount\n")

for category, amount in expenses.items():
    file.write(f"{category},{amount}\n")

file.close()

print("\nCSV file saved.")
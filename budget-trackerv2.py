# version 2 : added a Warning

monthly_budget = float(input("Enter your monthly budget: "))

rent = float(input("Enter rent cost: "))
food = float(input("Enter food cost: "))
gas = float(input("Enter gas cost: "))
travel = float(input("Enter travel cost: "))
restaurants = float(input("Enter restaurant cost: "))

total_spent = rent + food + gas + travel + restaurants
remaining = monthly_budget - total_spent

print("\n----- Budget Summary -----")
print("Rent:", rent)
print("Food:", food)
print("Gas:", gas)
print("Travel:", travel)
print("Restaurants:", restaurants)

print("\nTotal Spent:", total_spent)
print("Remaining Budget:", remaining)

if remaining < 0:
    print("WARNING: You are over budget!")
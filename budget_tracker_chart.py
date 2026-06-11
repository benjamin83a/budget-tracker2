import matplotlib.pyplot as plt

categories = ["Food", "Gas", "Travel", "Restaurants"]
amounts = [400, 150, 250, 200]

plt.pie(amounts, labels=categories, autopct="%1.1f%%")
plt.title("Monthly Spending Breakdown")
plt.show()
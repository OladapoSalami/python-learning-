import budget

# 1. Create categories
food = budget.Category("Food")
clothing = budget.Category("Clothing")
auto = budget.Category("Auto")

# 2. Add some data
food.deposit(1000, "initial deposit")
food.withdraw(105.55, "groceries")
clothing.deposit(500, "initial deposit")
clothing.withdraw(50, "new shirt")
auto.deposit(1000, "initial deposit")
auto.withdraw(150, "gasoline")

# 3. Print the results
print(food)
print(budget.create_spend_chart([food, clothing, auto]))

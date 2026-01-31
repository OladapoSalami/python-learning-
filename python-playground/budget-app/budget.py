"""
Project: Budget App (freeCodeCamp Certification)
Description: A system to manage budget categories, track deposits/withdrawals, 
             and visualize spending distribution.
Skills: Object-Oriented Programming (Classes), List Comprehensions, String Formatting.
"""

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Professional formatting for the budget readout
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    """Generates a bar chart showing the percentage spent per category."""
    withdrawals = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])
        withdrawals.append(total)

    total_withdrawals = sum(withdrawals)
    percentages = []
    for amount in withdrawals:
        if total_withdrawals > 0:
            percentages.append(int((amount / total_withdrawals) * 100 // 10) * 10)
        else:
            percentages.append(0)

    res = "Percentage spent by category"
    for i in range(100, -1, -10):
        res += "\n" + str(i).rjust(3) + "| "
        for p in percentages:
            res += "o  " if p >= i else "   "
    
    res += "\n    " + "-" * (len(categories) * 3 + 1)

    cat_names = [cat.name for cat in categories]
    max_len = max(len(name) for name in cat_names)
    
    for i in range(max_len):
        res += "\n     " 
        for name in cat_names:
            res += (name[i] + "  ") if i < len(name) else "   "
                
    return res

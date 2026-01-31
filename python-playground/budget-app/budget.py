"""
Project: Budget App Certification Project
Goal: Calculate spending percentages and display a vertical bar chart.
Skills: List comprehensions, string manipulation, and mathematical rounding.
"""

def create_spend_chart(categories):
    # 1. Calculate total withdrawals for each category
    withdrawals = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])
        withdrawals.append(total)

    # 2. Convert amounts to percentages (rounded down to the nearest 10)
    total_withdrawals = sum(withdrawals)
    percentages = []
    for amount in withdrawals:
        if total_withdrawals > 0:
            # Using integer division to get the floor of the percentage
            percentages.append(int((amount / total_withdrawals) * 100 // 10) * 10)
        else:
            percentages.append(0)

    # 3. Build the chart string
    res = "Percentage spent by category"

    # Create the Y-axis and the "o" bars
    for i in range(100, -1, -10):
        res += "\n" + str(i).rjust(3) + "| "
        for p in percentages:
            if p >= i:
                res += "o  "
            else:
                res += "   "
    
    # Create the X-axis separator
    res += "\n    " + "-" * (len(categories) * 3 + 1)

    # 4. Format the category names vertically
    cat_names = [cat.name for cat in categories]
    max_len = max(len(name) for name in cat_names)
    
    for i in range(max_len):
        res += "\n     " 
        for name in cat_names:
            if i < len(name):
                res += name[i] + "  "
            else:
                res += "   " 
                
    return res

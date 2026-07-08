sales = [150, 400, 30, 800, 200, 50, 600]

total = 0
for s in sales:
    total = total + s

highest = sales[0]
for s in sales:
    if s > highest:
        highest = s

lowest = sales[0]
for s in sales:
    if s < lowest:
        lowest = s

print("Total Sales:", total)
print("Max Sale:", highest)
print("Min Sale:", lowest)

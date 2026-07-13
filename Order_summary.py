orders = [
    {"item": "apple", "price": 10},
    {"item": "banana", "price": 5},
    {"item": "apple", "price": 10},
    {"item": "orange", "price": 8},
    {"item": "banana", "price": 5}
]

summary = {}

for order in orders:
    item = order["item"]
    price = order["price"]
    if item in summary:
        summary[item]["count"] += 1
        summary[item]["total_price"] += price
    else:
        summary[item] = {"count": 1, "total_price": price}

print(summary)

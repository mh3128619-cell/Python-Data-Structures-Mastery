from collections import Counter

all_transactions = [101, 102, 103, 101, 104, 102, 105, 101]
returned_products = [102, 104]

sales_count = Counter(all_transactions)
returns_count = Counter(returned_products)

final_inventory = {}
for product in set(all_transactions):
    net = sales_count[product] - returns_count.get(product, 0)
    if net > 0:
        final_inventory[product] = net

print("Final inventory after returns:", final_inventory)

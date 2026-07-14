transactions = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": 750},
    {"id": 3, "amount": 300},
    {"id": 4, "amount": 1200},
    {"id": 5, "amount": 50},
    {"id": 6, "amount": 900}
]
high_value_gen = (t["amount"] for t in transactions if t["amount"] > 500)

for amount in high_value_gen:
    print(f"High value transaction: {amount}")

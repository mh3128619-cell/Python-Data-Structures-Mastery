prices = [50, 120, 300, 80, 200]
final_prices = [p * 0.8 if p > 100 else p for p in prices]
print(final_prices)

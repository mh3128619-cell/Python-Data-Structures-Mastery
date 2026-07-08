products = ["Laptop", "Mouse", "Keyboard", "Monitor", "USB Cable"]
prices = [12000, 250, 500, 3000, 100]

for i in range(len(prices)):
    if prices[i] > 1000:
        prices[i] = prices[i] * 0.9

for i in range(len(products)):
    print(products[i] + ": " + str(prices[i]))

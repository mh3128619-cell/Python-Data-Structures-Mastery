numbers = [1, 4, 9, 16, 25, 36, 49, 64]
even_numbers = []

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])

print(even_numbers)

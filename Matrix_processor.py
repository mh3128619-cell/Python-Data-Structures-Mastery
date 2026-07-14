matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [item * 10 for sublist in matrix for item in sublist if item % 2 != 0]
print(result)

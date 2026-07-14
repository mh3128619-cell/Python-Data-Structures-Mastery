matrix = [[1, 2, 3], [4, 8, 6], [7, 2, 9]]
result = [max(sublist) for sublist in matrix if max(sublist) > 5]
print(result)

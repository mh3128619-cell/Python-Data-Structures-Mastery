coordinates = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (7, 8)]
unique_coordinates = []

for coord in coordinates:
    if coord not in unique_coordinates:
        unique_coordinates.append(coord)

print(unique_coordinates)

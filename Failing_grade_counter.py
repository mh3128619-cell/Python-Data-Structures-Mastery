grades = [55, 40, 90, 85, 30, 60, 45]

count = sum(1 for grade in grades if (grade - 50) < 0)

print(f"Count of negative differences: {count}")

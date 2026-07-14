large_numbers = range(1000000)

squares_gen = (num * num for num in large_numbers)

count = 0
for square in squares_gen:
    print(square)
    count += 1
    if count == 5:
        break

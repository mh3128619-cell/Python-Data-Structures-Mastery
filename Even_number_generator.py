def even_numbers_generator(numbers_list):
    for num in numbers_list:
        if num % 2 == 0:
            yield num

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_gen = even_numbers_generator(numbers)

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

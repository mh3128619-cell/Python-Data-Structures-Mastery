numbers=(45,12,89,3,24,56,77,10,5)
even_numbers=[]
odd_numbers=[]

for i in numbers:
  if i%2==0:
    even_numbers.append(i)
  else:
    odd_numbers.append(i)

  even_numbers.sort()
  odd_numbers.sort()
print(even_numbers)
print(odd_numbers)

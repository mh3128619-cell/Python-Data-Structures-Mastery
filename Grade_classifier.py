scores=[45,92,70,30,85,95]

list_of_grades=["excellent" if item > 90 else "pass" for item in scores if item>=50]
print(list_of_grades)

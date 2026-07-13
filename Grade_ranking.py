grades = {"Ahmed": 85, "Sara": 92, "Mohamed": 78, "Ali": 95}

sorted_grades = dict(sorted(grades.items(), key=lambda item: item[1], reverse=True))
print(sorted_grades)

students_grades = {
    "Ahmed": [85, 90],
    "Sara": [95, 88],
    "Mohamed": [70, 75]
}

averages = {}

def calculate_average(grades):
    return sum(grades) / len(grades)

for student, grades in students_grades.items():
    averages[student] = calculate_average(grades)

print(averages)

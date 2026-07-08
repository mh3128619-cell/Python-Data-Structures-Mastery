students = (("Ahmed", 75), ("Sara", 92), ("Mohamed", 84), ("Mona", 95), ("Ali", 60))
top_students = []
total_scores = 0

for student in students:
    total_scores += student[1]
    if student[1] >= 90:
        top_students.append(student)

average_score = total_scores / len(students)

print("Top Students:", top_students)
print("Average Score:", average_score)

search_name = input("Enter the name of the student: ")
found = False
for student in students:
    if student[0] == search_name:
        print("Student found:", student)
        found = True
        break

if not found:
    print("Student not found.")

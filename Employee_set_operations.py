attendance_today = {"Ahmed", "Sara", "Mohamed", "Ali", "Mona", "Omar"}
sales_department = {"Ahmed", "Sara", "Hassan", "Laila"}
it_department = {"Mohamed", "Ali", "Omar", "Youssef", "Khaled"}

present_sales = sales_department.intersection(attendance_today)
print(f"Present Sales employees: {present_sales}")

absent_it = it_department.difference(attendance_today)
print(f"Absent IT employees: {absent_it}")

are_departments_distinct = sales_department.isdisjoint(it_department)
print(f"Are departments completely distinct? {are_departments_distinct}")

all_employees = sales_department.union(it_department)
print(f"All employees in both departments: {all_employees}")

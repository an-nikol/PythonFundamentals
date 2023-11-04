# dictionary with nested lists
# one student (key) with multiple marks(values)

n = int(input())

grades_by_student = {}
for i in range(n):
    student_name = input()
    student_grade = float(input())

    if student_name not in grades_by_student:
        # create a list as value
        grades_by_student[student_name] = {}
    grades_by_student[student_name] = student_grade

for student, grades in grades_by_student.items():
    average_grade = sum(grades) / len(grades)
    if average_grade < 4.50:
        continue
    print(f'{student} -> {average_grade:.2f}')

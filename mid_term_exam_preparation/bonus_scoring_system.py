import math

number_of_students = int(input())
number_of_lectures = int(input())
bonus = int(input())

student_with_max_bonus = 0
attendances_of_student_with_max_bonus = 0
current_bonus = 0
for current_student in range(1, number_of_students + 1):
    attendance_per_student = int(input())
    current_bonus = (attendance_per_student / number_of_lectures) * (5 + bonus)
    if current_bonus > student_with_max_bonus:
        student_with_max_bonus = current_bonus
        attendances_of_student_with_max_bonus = attendance_per_student

print(f'Max Bonus: {math.ceil(student_with_max_bonus)}.')
print(f'The student has attended {attendances_of_student_with_max_bonus} lectures.')


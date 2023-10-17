first_employee = int(input())  # handling number of students per hour
second_employee = int(input())
third_employee = int(input())

total_students_count = int(input())
count_of_hours = 0
total_answered_questions_per_hour = first_employee + second_employee + third_employee

while total_students_count > 0:
    total_students_count -= total_answered_questions_per_hour
    count_of_hours += 1
    if count_of_hours % 4 == 0:
        count_of_hours += 1
        continue

print(f'Time needed: {count_of_hours}h.')

name_and_points = {}
course_and_names = {}

while True:
    command = input()
    if command == 'exam finished':
        break

    student_info = command.split('-')
    name = student_info[0]
    if 'banned' in command:
        del name_and_points[name]

    else:
        programming_course = student_info[1]
        points = int(student_info[2])
        if name not in name_and_points:
            name_and_points[name] = []
        name_and_points[name].append(points)

        if programming_course not in course_and_names:
            course_and_names[programming_course] = 0
        # add submissions
        course_and_names[programming_course] += 1

print('Results:')
for curr_name in name_and_points:
    print(f'{curr_name} | {max(name_and_points[curr_name])}')

print('Submissions:')

for curr_course in course_and_names:
    print(f'{curr_course} - {course_and_names[curr_course]}')

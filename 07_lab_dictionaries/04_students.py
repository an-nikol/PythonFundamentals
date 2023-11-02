# nested dictionaries

data = input()
courses = {}

while ':' in data:
    student_name, student_id, course_name = data.split(':')
    # create a key course if it does not exist
    if course_name not in courses:
        courses[course_name] = {student_id: student_name}
    else:
        # if the key-course exists add another dictionary-value to the existing key
        # the courses[course_name] indicates the data type(dict) that we are adding it to
        courses[course_name][student_id] = student_name
    data = input()


# format the input if the data is programming_basics
course_name = ' '.join(data.split('_'))

# we are searching the courses dict based on the key which is the course type (e.g. fundamentals)
students_name_and_id = courses[course_name]

for student_id, student_name in students_name_and_id.items():
    print(f"{student_name} - {student_id}")
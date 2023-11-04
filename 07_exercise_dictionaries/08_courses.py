# nested dictionary
# one course(key) with multiple students (values)
command = input()

dict_course = {}
while command != "end":
    course_name, student_name = command.split(" : ")
    if course_name not in dict_course:
        # create an empty dict for each course. Then add a nested key(name) and a nested value(name),/
        # e.g. ('PB': {'Jake':'Jake'})
        dict_course[course_name] = {}
    dict_course[course_name][student_name] = student_name
    command = input()

for key in dict_course:
    print(f"{key}: {len(dict_course[key])}")
    # here use only the value of the created nested dict
    for nested_key, nested_value in dict_course[key].items():
        print(f"-- {nested_value}")
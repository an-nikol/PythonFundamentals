contests_and_pass = {}
user_course_points = {}

command = input()
while command != 'end of contests':
    contest, password = command.split(':')
    if contest not in contests_and_pass:
        contests_and_pass[contest] = password
    command = input()
line = input()

while line != 'end of submissions':
    contest, password, username, points = line.split('=>')
    if contest in contests_and_pass and password == contests_and_pass[contest]:
        if username not in user_course_points:
            user_course_points[username] = {}
        if contest not in user_course_points[username]:
            user_course_points[username][contest] = {}
            user_course_points[username][contest] = 0

        if user_course_points[username][contest] < int(points):
            user_course_points[username][contest] = int(points)
    line = input()

best_candidate = ''
max_total_points = 0


for key in user_course_points:
    current_total_points = 0
    for nested_key, nested_value in user_course_points[key].items():
        current_total_points += nested_value
        if current_total_points > max_total_points:
            max_total_points = current_total_points
            best_candidate = key

print(f'Best candidate is {best_candidate} with total {max_total_points} points.')
print('Ranking:')
sorted_dict = dict(sorted(user_course_points.items()))

for key, value in sorted_dict.items():
    print(f"{key}")
    results_in_descending_order = dict(sorted(sorted_dict[key].items(), key=lambda x: x[1], reverse=True))
    for nested_key, nested_value in results_in_descending_order.items():
        print(f"#  {nested_key} -> {nested_value}")
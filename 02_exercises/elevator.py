number_of_people = int(input())
elevator_capacity = int(input())
counter_course = 0

while number_of_people > 0:
    number_of_people -= elevator_capacity
    counter_course += 1

print(counter_course)
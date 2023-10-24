import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

first_line = tuple([math.floor(x1), math.floor(y1)])
second_line = tuple([math.floor(x2), math.floor(y2)])

sum_first_line = 0
sum_second_line = 0

for num in first_line:
    sum_first_line += math.floor(abs(num))

for num2 in second_line:
    sum_second_line += math.floor(abs(num2))


def closest_point(first_length, second_length):
    if first_length <= second_length:
        print(first_line)
    else:
        print(second_line)

closest_point(sum_first_line, sum_second_line)
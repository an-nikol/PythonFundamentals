import math

# create a tuple which items are formatted to the lower integer, which are floats and add each of them in a tuple
points = tuple(math.floor(float(input())) for point in range(4))

# find the abs sum of the two points

# start with the first half of the tuple
sum_x = sum([abs(num) for num in points[:2]])
# continue with the second half
sum_y = sum([abs(num) for num in points[2:]])


# define a function to find the closes points
def closer_set_of_points(first_point, second_point):
    # the point that is closer to 0 shall be printed
    if first_point <= second_point:
        return points[:2]
    else:
        return points[2:]

print(closer_set_of_points(sum_x, sum_y))

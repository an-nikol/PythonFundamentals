number_of_snowballs = int(input())

highest_snowball_score = 0
weight_of_best_ball = 0
time_for_best_ball = 0
quality_for_best_ball = 0
for snowball in range(1, number_of_snowballs + 1):
    weight = int(input())
    time_to_hit_the_target = int(input())
    quality = int(input())
    current_snowball_score = (weight / time_to_hit_the_target) ** quality
    if current_snowball_score > highest_snowball_score:
        highest_snowball_score = int(current_snowball_score)
        weight_of_best_ball = weight
        time_for_best_ball = time_to_hit_the_target
        quality_for_best_ball = quality

print(f'{weight_of_best_ball} : {time_for_best_ball} = {highest_snowball_score} ({quality_for_best_ball})')

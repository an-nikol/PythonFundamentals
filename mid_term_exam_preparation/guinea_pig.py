qty_of_total_food_in_kgs = float(input())
qty_of_hay_in_kgs = float(input())
qty_of_cover_in_kgs = float(input())
weight = float(input()) * 1000

qty_of_total_food_in_gr = qty_of_total_food_in_kgs * 1000
qty_of_hay_in_gr = qty_of_hay_in_kgs * 1000
qty_of_cover_in_gr = qty_of_cover_in_kgs * 1000

food_per_day_gr = 300

is_food_enough = True
for day in range(1, 30 + 1):
    qty_of_total_food_in_gr -= food_per_day_gr
    if day % 2 == 0:
        qty_of_hay_in_gr -= qty_of_total_food_in_gr * 0.05
    if day % 3 == 0:
        qty_of_cover_in_gr -= weight * (1/3)

    if qty_of_total_food_in_gr <= 0 or qty_of_hay_in_gr <= 0 or qty_of_cover_in_gr <= 0:
        is_food_enough = False
        print('Merry must go to the pet store!')
        break

if is_food_enough:
    print(f'Everything is fine! Puppy is happy! Food: {qty_of_total_food_in_gr / 1000:.2f}, '
          f'Hay: {qty_of_hay_in_gr / 1000:.2f}, Cover: {qty_of_cover_in_gr / 1000:.2f}.')

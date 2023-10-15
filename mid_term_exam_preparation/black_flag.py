number_of_days = int(input())
plunder_per_day = int(input())
target_plunder = float(input())

total_plunder = 0
for day in range(1, number_of_days + 1):
    total_plunder += plunder_per_day
    if day % 3 == 0:
        total_plunder += plunder_per_day / 2
    if day % 5 == 0:
        total_plunder *= 0.70

if total_plunder >= target_plunder:
    print(f'Ahoy! {total_plunder:.2f} plunder gained.')
else:
    diff = target_plunder - total_plunder
    plunder_left = target_plunder - diff
    percentage = (plunder_left / target_plunder) * 100
    print(f'Collected only {percentage:.2f}% of the plunder.')

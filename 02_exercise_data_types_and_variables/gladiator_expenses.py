number_of_lost_fights = int(input())
price_helmet = float(input())
price_sword = float(input())
price_shield = float(input())
price_armour = float(input())

counter_expenses = 0
times_shield_broken = 0
for fight in range(1, number_of_lost_fights + 1):
    if fight % 2 == 0:
        counter_expenses += price_helmet
    if fight % 3 == 0:
        counter_expenses += price_sword
        if fight % 2 == 0:
            counter_expenses += price_shield
            times_shield_broken += 1
            if times_shield_broken % 2 == 0:
                counter_expenses += price_armour

print(f'Gladiator expenses: {counter_expenses:.02f} aureus')
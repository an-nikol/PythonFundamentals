budget = float(input())
price_flour_1_kg = float(input())
price_one_pack_eggs = price_flour_1_kg * 0.75
price_milk_250_ml = (price_flour_1_kg * 1.25) / 4
price_1_loaf_bread = price_flour_1_kg + price_one_pack_eggs + price_milk_250_ml

counter_coloured_eggs = 0
counter_bread_loaves = 0

while True:

    if budget <= price_1_loaf_bread:
        print \
            (f"You made {counter_bread_loaves}\
             loaves of Easter bread! Now you have {counter_coloured_eggs} eggs and {budget:.2f}BGN left.")

        break

    budget -= price_1_loaf_bread
    counter_bread_loaves += 1
    counter_coloured_eggs += 3

    if counter_bread_loaves % 3 == 0:
        counter_coloured_eggs -= counter_bread_loaves - 2

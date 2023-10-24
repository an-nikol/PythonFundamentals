import math

budget = float(input())
number_of_students = int(input())
price_for_package_of_flour = float(input())
price_for_one_egg = float(input())
price_for_one_apron = float(input())

free_packages = 0


for student in range(1, number_of_students + 1):
    # free flour
    if student % 5 == 0:
        free_packages += 1

number_aprons = math.ceil((number_of_students + (number_of_students * 0.20)))

total_price = (price_for_one_apron * number_aprons) + \
              (price_for_one_egg * 10 * number_of_students) + (price_for_package_of_flour *
                                                               (number_of_students - free_packages))


diff = total_price - budget

if total_price <= budget:
    print(f'Items purchased for {total_price:.2f}$.')

else:
    print(f'{diff:.2f}$ more needed.')

import re

text = input()

total_calories = 0
calories_per_day = 2000
pattern = r'([#|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'


# returns tuples of groups
matches = re.findall(pattern, text)

for match in matches:
    calories = int(match[3])
    total_calories += calories

days = total_calories // calories_per_day

print(f"You have food to last you for: {days} days!")
for match in matches:
    product_item = match[1]
    exp_date = match[2]
    calories = int(match[3])
    print(f"Item: {product_item}, Best before: {exp_date}, Nutrition: {calories}")

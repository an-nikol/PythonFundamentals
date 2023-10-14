list_of_numbers = list(map(int, input().split(', ')))

current_group = 10

while list_of_numbers:
    filtered_numbers_for_current_group = [number for number in list_of_numbers if number <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers_for_current_group}")
    current_group += 10
    list_of_numbers = [number for number in list_of_numbers if number not in filtered_numbers_for_current_group]
# split the string into a list
money_as_string = input().split(", ")
number_of_beggars = int(input())
money_as_integers = []

# convert the strings into integers (one by one!)
for current_money in money_as_string:
    money_as_integers.append(int(current_money))

# create a list to store the final result
final_sums = []

# add each sum of a beggar
start_index = 0

while start_index < number_of_beggars:
    current_beggar_sum = 0
    # start from the beginning of the list, go to the end of the list, with a step of the number of beggars
    # the start of the list changes every time!
    for current_index in range(start_index, len(money_as_integers), number_of_beggars):
        # add the value of the current position to the current sum
        current_beggar_sum += money_as_integers[current_index]
    final_sums.append(current_beggar_sum)
    start_index += 1

print(final_sums)

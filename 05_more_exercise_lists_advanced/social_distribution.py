list_of_population = [int(num) for num in input().split(', ')]
minimum_wealth = int(input())

is_equal = True
for current_population in range(len(list_of_population)):
    max_value = max(list_of_population)
    idx_of_wealthiest_person = list_of_population.index(max_value)
    if list_of_population[current_population] < minimum_wealth:
        diff = minimum_wealth - list_of_population[current_population]
        list_of_population[idx_of_wealthiest_person] -= diff
        list_of_population[current_population] = minimum_wealth

for population in range(len(list_of_population)):
    if list_of_population[population] < minimum_wealth:
        is_equal = False
        print('No equal distribution possible')
        break

if is_equal:
    print(list_of_population)

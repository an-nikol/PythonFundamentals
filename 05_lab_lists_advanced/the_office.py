def multiply_happiness(all_happiness, factor):
    list_of_happiness = []
    employee_counter = 0
    happy_employees = 0
    total_happiness = 0

    for happiness in all_happiness:
        list_of_happiness.append(happiness * factor)
        employee_counter += 1

    for happiness in list_of_happiness:
        total_happiness += happiness

    average = total_happiness / employee_counter

    for final_happiness in list_of_happiness:
        if final_happiness >= average:
            happy_employees += 1

    if happy_employees >= employee_counter // 2:
        print(f'Score: {happy_employees}/{employee_counter}. Employees are happy!')
    else:
        print(f'Score: {happy_employees}/{employee_counter}. Employees are not happy!')


all_employees_current_happiness = list(map(int, input().split()))
happiness_factor = int(input())
multiply_happiness(all_employees_current_happiness, happiness_factor)

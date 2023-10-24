number = int(input())

def loading_bar(n):
    is_complete = False
    counter_for_percentages = 0

    list_loading = []
    for percent in range(1, (n // 10) + 1):
        percent_bar = '%'
        list_loading.append(percent_bar)
        counter_for_percentages += 1

    if counter_for_percentages == 10:
        is_complete = True

    for dot in range((n//10), 10):
        dot_symbol = '.'
        list_loading.append(dot_symbol)
    joined_list_percentages = ''.join(list_loading)

    if is_complete:
        print(f'{n}% Complete!')
        print(f'[{joined_list_percentages}]')
    else:
        print(f'{n}% [{joined_list_percentages}]')
        print('Still loading...')

loading_bar(number)

# dict comprehension and zip method

my_dict = {key:value for key, value in zip(input().split(', '), input().split(', '))}

for key, value in my_dict.items():
    print(f'{key} -> {value}')
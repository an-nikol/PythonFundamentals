# nested dictionaries
dict_companies = {}

command = input()
while command != 'End':
    company, employee_id = command.split(' -> ')

    if company not in dict_companies:
        dict_companies[company] = {}
    dict_companies[company][employee_id] = employee_id

    command = input()

for key, value in dict_companies.items():
    print(f"{key}")
    for nested_key, nested_value in dict_companies[key].items():
        print(f"-- {nested_key}")


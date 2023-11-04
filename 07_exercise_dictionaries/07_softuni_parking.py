number_of_users = int(input())
dict_of_users = {}
for current_user in range(number_of_users):
    user_info = input().split()
    command, user_name = user_info[0], user_info[1]
    if command == 'register':
        car_number = user_info[2]
        if user_name not in dict_of_users:
            dict_of_users[user_name] = car_number
        else:
            print(f'ERROR: already registered with plate number {car_number}')
            continue

        print(f'{user_name} registered {car_number} successfully')

    elif command == 'unregister':
        if user_name not in dict_of_users:
            print(f'ERROR: user {user_name} not found')
            continue
        else:
            print(f'{user_name} unregistered successfully')
            # after unregistration delete the kvp
            del dict_of_users[user_name]

for key, value in dict_of_users.items():
    print(f'{key} => {value}')
def find_the_data_type(type, operation):
    if type == 'int':
        result = int(operation) * 2
        print(result)
    elif type == 'real':
        result = float(operation) * 1.5
        print(f'{result:.2f}')
    elif type == 'string':
        print(f'${operation}$')


data_type = input()
activity = input()

find_the_data_type(data_type, activity)


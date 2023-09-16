is_voldemort = False
while True:
    name = input()
    if name == 'Voldemort':
        print('You must not speak of that name!')
        is_voldemort = True
        break
    elif name == 'Welcome!':
        break

    length = len(name)
    if length < 5:
        print(f'{name} goes to Gryffindor.')
    elif length == 5:
        print(f'{name} goes to Slytherin.')
    elif length == 6:
        print(f'{name} goes to Ravenclaw.')
    elif length > 6:
        print(f'{name} goes to Hufflepuff.')

if not is_voldemort:
    print('Welcome to Hogwarts.')

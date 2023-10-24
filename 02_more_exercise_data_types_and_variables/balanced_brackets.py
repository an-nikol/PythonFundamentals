number = int(input())

# check the number of open and closed brackets
counter = 0
for line in range(number):
    current_symbol = input()
    if '(' in current_symbol:
        counter += 1
    elif ')' in current_symbol:
        counter -= 1
    # if some brackets are lacking or there is a surplus of brackets
    if 0 != counter != 1:
        print('UNBALANCED')
        break
else:
    print('BALANCED')

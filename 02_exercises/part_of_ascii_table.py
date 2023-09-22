start_index = int(input())
end_index = int(input())

for index in range(start_index, end_index + 1):
    index_to_char = chr(index)
    print(f'{index_to_char} ',end='')
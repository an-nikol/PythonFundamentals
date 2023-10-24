number_of_chars = int(input())

sum = 0
for char in range(1, number_of_chars + 1):
    current_char = input()
    char_to_code = ord(current_char)
    sum += char_to_code

print(f'The sum equals: {sum}')
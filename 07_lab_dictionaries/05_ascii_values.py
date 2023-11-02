# dict comprehension
chars_info = input().split(', ')

print({char: ord(char) for char in chars_info})

text = input()
digits = ''
chars = ''
other = ''
for symbol in text:
    if symbol.isdigit():
        digits += symbol
    elif symbol.isalpha():
        chars += symbol
    else:
        other += symbol


print(digits)
print(chars)
print(other)
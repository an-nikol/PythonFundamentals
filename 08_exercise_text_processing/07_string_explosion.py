text = input()
final_string = ""
strength = 0

for index in range(len(text)):
    # We have explosion
    if strength > 0 and text[index] != ">":
        strength -= 1
    # We have explosion mark
    elif text[index] == ">":
        final_string += text[index]
        strength += int(text[index + 1])
    # We have no explosion -> normal character
    else:
        final_string += text[index]
print(final_string)
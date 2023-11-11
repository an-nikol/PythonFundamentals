text = input()

result = []

for char in text:
    # check if the list is empty ot the last char in the list is not equal to the current one
    if not result or result[-1] != char:
        result.append(char)

print(f"{''.join(result)}")



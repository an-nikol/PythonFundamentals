first_char = input()
second_char = input()


def find_chars_in_between(first_letter, second_letter):
    position_first_letter = ord(first_letter) + 1
    position_second_letter = ord(second_letter)
    list_of_chars_in_between = []
    for current_char_value in range(position_first_letter, position_second_letter):
        ascii_value_to_char = chr(current_char_value)
        list_of_chars_in_between.append(ascii_value_to_char)

    result = ' '.join(list_of_chars_in_between)
    return result


print(find_chars_in_between(first_char, second_char))

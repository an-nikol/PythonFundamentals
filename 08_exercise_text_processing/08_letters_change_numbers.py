def upper_letter_position(letter):
    return ord(letter) - 64


def lower_letter_position(letter):
    return ord(letter) - 96


words = input().split()
total_sum = 0

# find how to store each value of the string

for word in words:
    number_curr_word = int(word[1:-1])
    if word[0].isupper():
        let_pos = upper_letter_position((word[0]))
        result = number_curr_word / let_pos
        total_sum += result

    else:
        let_pos = lower_letter_position((word[0]))
        result = number_curr_word * let_pos
        total_sum = result


    if word[-1].isupper():
        let_pos = upper_letter_position(word[-1])
        total_sum -= let_pos

    else:
        let_pos = lower_letter_position((word[-1]))
        total_sum += let_pos



print(total_sum)
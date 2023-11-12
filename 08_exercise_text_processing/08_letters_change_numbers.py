def upper_letter_position(letter):
    return ord(letter) - 64


def lower_letter_position(letter):
    return ord(letter) - 96


words = input().split()
current_sums = {}


for word in words:
    number_curr_word = int(word[1:-1])
    if word not in current_sums:
        current_sums[word] = 0

    if word[0].isupper():
        let_pos = upper_letter_position((word[0]))
        result = number_curr_word / let_pos
        current_sums[word] += result

    else:
        if word not in current_sums:
            current_sums[word] = 0
        let_pos = lower_letter_position((word[0]))
        result = number_curr_word * let_pos
        current_sums[word] += result

    if word[-1].isupper():
        if word not in current_sums:
            current_sums[word] = 0
        let_pos = upper_letter_position(word[-1])
        current_sums[word] -= let_pos

    else:
        if word not in current_sums:
            current_sums[word] = 0
        let_pos = lower_letter_position((word[-1]))
        current_sums[word] += let_pos

total_sum = 0
for key in current_sums:
    total_sum += current_sums[key]

print(f'{total_sum:.2f}')
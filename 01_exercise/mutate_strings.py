first_string = input()
second_string = input()

# variable to store the first string to check for uniqueness
last_printed_string = first_string

for char in range(len(first_string)):
    # slice the two words in left and right part
    # your new word will start with the char of the second word(left side)
    left_part = second_string[:char + 1] # the end is the current char
    # your new word's second part will take the right side of the second string
    right_part = first_string[char + 1:] # the start is the next char of the first word
    # check for uniqueness
    transformed_word = left_part + right_part
    if last_printed_string != transformed_word:
        print(transformed_word)
        # update the last printed string
        last_printed_string = transformed_word

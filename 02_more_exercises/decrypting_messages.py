key = int(input())
number_of_letters = int(input())

decrypted_word = ''

for letter in range(1, number_of_letters + 1):
    current_letter = input()
    letter_to_ascii_value = ord(current_letter)
    decrypted_letter = letter_to_ascii_value + key
    decrypted_word += chr(decrypted_letter)

print(decrypted_word)

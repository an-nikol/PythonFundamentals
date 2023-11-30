import re

text = input()
mirror_words = []
pattern = r'([#@]){1}([A-z]{3,})\1{2}([A-z]{3,})\1'


matches = list(re.finditer(pattern, text))

for match in matches:
    first_word = match.group(2)
    second_word = match.group(3)
    if first_word == second_word[::-1]:
        mirror_words.append(f"{first_word} <=> {second_word}")

if matches:
    print(f'{len(matches)} word pairs found!')
else:
    print('No word pairs found!')

if mirror_words:
    print('The mirror words are:')
    print(f"{', '.join(mirror_words)}")
else:
    print('No mirror words!')



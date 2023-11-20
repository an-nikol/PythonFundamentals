import re

number_of_messages = int(input())
required_letters = ['s', 't', 'a', 'r']
pattern = r'.*@(?P<planet>[A-Z][a-z]+)[^\@\-\!\:\>]*:(?P<population>\d+)' \
          r'[^\@\-\!\:\>]*\!(?P<attack_type>A|D)\![^\@\-\!\:\>]*\->(?P<soldiers>\d+).*'

counter_for_attacked_planets = 0
counter_for_destroyed_planets = 0

list_of_attacked_planets = []
list_of_destroyed_planets = []

for message in range(number_of_messages):
    # find the current count
    counter_for_occurred_letters = 0
    decrypted_message = ''
    current_message = input()
    current_message_lower = current_message.lower()
    for letter in current_message_lower:
        if letter in required_letters:
            counter_for_occurred_letters += 1
    # subtract the current count
    for char in current_message:
        new_char_ord = ord(char) - counter_for_occurred_letters
        new_char = chr(new_char_ord)

        decrypted_message += new_char

    match = re.search(pattern, decrypted_message)
    if match:
        planet_name = match.group(1)
        attacked_or_destroyed_planet = match.group(3)

        if attacked_or_destroyed_planet == 'A':
            counter_for_attacked_planets += 1
            list_of_attacked_planets.append(planet_name)
        elif attacked_or_destroyed_planet == 'D':
            list_of_destroyed_planets.append(planet_name)
            counter_for_destroyed_planets += 1

print(f'Attacked planets: {counter_for_attacked_planets}')
if counter_for_attacked_planets:
    sorted_attacked_planets = sorted(list_of_attacked_planets)
    for planet in sorted_attacked_planets:
        print(f'-> {planet}')

print(f'Destroyed planets: {counter_for_destroyed_planets}')
if counter_for_destroyed_planets:
    sorted_destroyed_planets = sorted(list_of_destroyed_planets)
    for planet in sorted_destroyed_planets:
        print(f'-> {planet}')

# sort
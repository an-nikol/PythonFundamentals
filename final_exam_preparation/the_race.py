import re

pattern = r'([#$%*&])([A-Za-z]+)\1=(\d+)(!!)(.*)'

while True:
    string = input()
    match = re.search(pattern, string)
    if match:
        symbol, name, length, symbols, encrypted_geohash = match.groups()
        encrypted_geohash = encrypted_geohash[:int(length)]
        decrypted_geohash = ''.join(chr(ord(char) + int(length)) for char in encrypted_geohash)
        print(f'Coordinates found! {name} -> {decrypted_geohash}')
        break
    else:
        print('Nothing found!')



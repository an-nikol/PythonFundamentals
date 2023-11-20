number_of_pieces = int(input())

dict_piece_compositor = {}
dict_piece_key = {}

for curr_piece in range(number_of_pieces):
    pieces_info = input().split('|')
    piece, composer, key = pieces_info[0], pieces_info[1], pieces_info[2]
    if piece not in dict_piece_compositor:
        dict_piece_compositor[piece] = composer
    if piece not in dict_piece_key:
        dict_piece_key[piece] = key

# commands
command = input()

while command != 'Stop':
    command = command.split('|')
    instruction, piece = command[0], command[1]
    if instruction == 'Add':
        composer = command[2]
        key = command[3]
        if piece not in dict_piece_compositor:
            dict_piece_compositor[piece] = composer
            dict_piece_key[piece] = key
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')

    elif instruction == 'Remove':
        if piece in dict_piece_compositor:
            del dict_piece_compositor[piece]
            print(f'Successfully removed {piece}!')
            if piece in dict_piece_key:
                del dict_piece_key[piece]
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif instruction == 'ChangeKey':
        new_key = command[2]
        if piece in dict_piece_key:
            dict_piece_key[piece] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    command = input()

for key in dict_piece_compositor:
        print(f'{key} -> Composer: {dict_piece_compositor[key]}, Key: {dict_piece_key[key]}')
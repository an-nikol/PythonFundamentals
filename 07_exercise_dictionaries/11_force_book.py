# each player - side
side_of_player = {}

# all players - to a concrete side
players_in_side = {}

while True:
    line = input()
    if line == 'Lumpawaroo':
        break

    if ' | ' in line:
        player_information = line.split(' | ')
        force_side = player_information[0]
        force_user = player_information[1]

        # guarantee that such a side will be created
        if force_side not in players_in_side:
            players_in_side[force_side] = []

        if force_user not in side_of_player:
            side_of_player[force_user] = force_side
            players_in_side[force_side].append(force_user)
    else:
        player_information = line.split(' -> ')
        force_user = player_information[0]
        force_side = player_information[1]

        # guarantee that such a side will be created
        if force_side not in players_in_side:
            players_in_side[force_side] = []

        players_in_side[force_side].append(force_user)
        # switch sides when the force user exists
        if force_user in side_of_player:
            old_side = side_of_player[force_user]
            players_in_side[old_side].remove(force_user)
            side_of_player[force_user] = force_user

        # when the force user does not exist (doing the same as above)
        else:
            side_of_player[force_user] = force_side

        print(f"{force_user} joins the {force_side} side!")
for side, members in players_in_side.items():
    if len(members) == 0:
        continue
    print(f'Side: {side}, Members: {len(members)}')

    for member in members:
        print(f'! {member}')
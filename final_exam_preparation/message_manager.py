username_sent_received_msg = {}
max_capacity = int(input()) # the sum of sent and received msg

command = input()

while command != 'Statistics':
    command_info = command.split('=')
    instruction = command_info[0]

    if instruction == 'Add':
        username, sent_msg, received_msg = command_info[1], int(command_info[2]), int(command_info[3])
        if username not in username_sent_received_msg:
            username_sent_received_msg[username] = {'sent': sent_msg, 'received': received_msg}
    elif instruction == 'Message':
        sender, receiver = command_info[1], command_info[2]
        if sender in username_sent_received_msg and receiver in username_sent_received_msg:
            username_sent_received_msg[sender]['sent'] += 1
            username_sent_received_msg[receiver]['received'] += 1
            if username_sent_received_msg[sender]['sent'] + username_sent_received_msg[sender]['received'] >= max_capacity:
                del username_sent_received_msg[sender]
                print(f'{sender} reached the capacity!')

            if username_sent_received_msg[receiver]['sent'] + username_sent_received_msg[receiver]['received'] >= max_capacity:
                del username_sent_received_msg[receiver]
                print(f'{receiver} reached the capacity!')
    elif instruction == 'Empty':
        username = command_info[1]
        if username == 'All':
            # might be del here
            username_sent_received_msg.clear()
        else:
            del username_sent_received_msg[username]
    command = input()

print(f'Users count: {len(username_sent_received_msg)}')

for user in username_sent_received_msg:
    print(f"{user} - {username_sent_received_msg[user]['sent'] + username_sent_received_msg[user]['received']}")

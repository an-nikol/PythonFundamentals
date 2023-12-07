# without ascending and descending order
followers_likes_comments = {}

command = input()

while command != 'Log out':
    command_info = command.split(': ')
    instruction = command_info[0]
    username = command_info[1]

    if instruction == 'New follower':
        if username not in followers_likes_comments:
            # do this for all below
            followers_likes_comments[username] = {'likes': 0, 'comments': 0}

    elif instruction == 'Like':
        likes = int(command_info[2])
        if username not in followers_likes_comments:
            followers_likes_comments[username] = {'likes': likes, 'comments': 0}
        else:
            followers_likes_comments[username]['likes'] += likes

    elif instruction == 'Comment':
        if username not in followers_likes_comments:
            followers_likes_comments[username] = {'likes': 0, 'comments': 1}
        else:
            followers_likes_comments[username]['comments'] += 1
    elif instruction == 'Blocked':
        if username in followers_likes_comments:
            del followers_likes_comments[username]
        else:
            print(f'{username} doesn\'t exist.')

    command = input()

print(f'{len(followers_likes_comments)} followers')

for follower in followers_likes_comments:
    print(f"{follower}: {followers_likes_comments[follower]['likes'] + followers_likes_comments[follower]['comments']}")




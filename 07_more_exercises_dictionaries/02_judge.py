contest_username = {}
individual_dict = {}
command = input()

while command != "no more time":
    data = command.split(' -> ')
    username, contest, points = data[0], data[1], int(data[2])
    contest_username[contest] = contest_username.get(contest, {})
    contest_username[contest][username] = contest_username[contest].get(username, 0)
    contest_username[contest][username] = max(points, contest_username[contest][username])
    command = input()


for contest in contest_username:
    print(f"{contest}: {len(contest_username[contest])} participants")
    for position, (user, score) in enumerate(sorted(contest_username[contest].items(), key=lambda x: (-x[1], x[0])), 1):
        print(f"{position}. {user} <::> {score}")
        individual_dict[user] = individual_dict.get(user, 0) + score

print("Individual standings:")
for position, (user, score) in enumerate(sorted(individual_dict.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{position}. {user} -> {score}")
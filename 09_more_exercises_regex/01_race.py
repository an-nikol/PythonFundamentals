names_info = {x: 0 for x in input().split(", ")}

info = input()
while info != "end of race":
    name, distance = "", []

    for char in info:
        if char.isdigit():
            distance.append(int(char))
        elif char.isalpha():
            name += char

    if name in names_info:
        names_info[name] += sum(distance)
    info = input()


names_info = sorted(names_info.items(), key=lambda x: -x[1])

print(f"1st place: {names_info[0][0]}")
print(f"2nd place: {names_info[1][0]}")
print(f"3rd place: {names_info[2][0]}")


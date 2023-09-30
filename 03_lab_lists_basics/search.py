number_of_lines = int(input())
magic_word = input()

string_list = []

for line in range(number_of_lines):
    current_word = input()
    string_list.append(current_word)
print(string_list)

# remove the strings we do not need
# we start in reverse order so we don't skip elements when removing
for i in range(len(string_list) - 1, -1, -1):
    element = string_list[i]
    if magic_word not in element:
        string_list.remove(element)
print(string_list)



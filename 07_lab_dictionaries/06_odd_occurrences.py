# make each word lower
word_keys = [current_item.lower() for current_item in input().split()]

my_dict_occur = {}

for current_key in word_keys:
    # add the kvp to the dict
    if current_key not in my_dict_occur:
        my_dict_occur[current_key] = 0
    # change the value of the kvp
    my_dict_occur[current_key] += 1

for key, value in my_dict_occur.items():
    if value % 2 != 0:
        print(key, end=' ')
original_list = input().split()
list_of_even_length = [word for word in original_list if len(word) % 2 == 0]

for word in list_of_even_length:
    print(str(word))

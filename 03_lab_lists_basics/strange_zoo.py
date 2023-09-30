string_head = input()
string_body = input()
string_tail = input()


temp = string_head
string_head = string_tail
string_tail = temp

filtered_list = [string_head, string_body, string_tail]

print(filtered_list)
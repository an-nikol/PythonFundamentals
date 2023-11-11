file = input().split("\\")

file_name = ''
file_type = ''
for idx in range(len(file)):
    if '.' in file[idx]:
        name_and_ext = file[idx].split('.')
        file_name = name_and_ext[0]
        file_type = name_and_ext[1]

print(f'File name: {file_name}')
print(f'File extension: {file_type}')

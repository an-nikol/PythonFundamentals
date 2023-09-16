divisor = int(input())
boundary = int(input())

current_number = 0
max_number = 0
# find the largest int N
for i in range(1, boundary + 1):
    if i % divisor == 0:
        current_number = i
        if current_number > max_number:
            max_number = current_number
print(max_number)

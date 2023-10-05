operator = input()
first_number = int(input())
second_number = int(input())


# declare a function that adds, subtracts etc
def calculation(operation, first_integer, second_integer):
    if operation == 'multiply':
        result = first_integer * second_integer
        return result
    elif operation == 'divide':
        result = first_integer // second_integer
        return result
    elif operation == 'add':
        result = first_integer + second_integer
        return result
    elif operation == 'subtract':
        result = first_integer - second_integer
        return result


# call the function
print(calculation(operator, first_number, second_number))

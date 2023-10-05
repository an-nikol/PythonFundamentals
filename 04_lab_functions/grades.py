# declare a function

def grade(score):
    if score < 3.00:
        return 'Fail'
    elif 3.00 <= score < 3.50:
        return 'Poor'
    elif 3.50 <= score < 4.50:
        return 'Good'
    elif 4.50 <= score < 5.50:
        return 'Very Good'
    else:
        return 'Excellent'


# read the user input
current_score = float(input())
# call the function
print(grade(current_score))

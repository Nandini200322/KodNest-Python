def check_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Read one integer
number = int(input())

# Call the function and store the returned value
result = check_sign(number)

# Print the returned value
print(result)
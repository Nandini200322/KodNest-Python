word = input()

first = int(input())
second = int(input())
third = int(input())

numbers = [first, second, third]
record = (first, second, third)

middle_string = word[1:-1]
first_two_number = numbers[:2]
reversed_tuple = record[::-1]

print(f"Middle: {middle_string}")
print(f"First Two: {first_two_number}")
print(f"Reversed Tuple: {reversed_tuple}")
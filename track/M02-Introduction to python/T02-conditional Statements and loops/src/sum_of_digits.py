number = int(input())
sum_of_digits = 0
while(number>0):
  sum_of_digits += number%10
  number //=10
print(f"sum of Digits: {sum_of_digits}")
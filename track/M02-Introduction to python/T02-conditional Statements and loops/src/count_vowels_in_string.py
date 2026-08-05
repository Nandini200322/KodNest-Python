text = input()
vowel_count = 0
for i in text.lower():
 if i in "aeiou":
   vowel_count += 1
print(f"Vowel Count: {vowel_count}")
import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

while True:
   try:
       password_length = int(input("Enter the desired password length (minimum 8): "))
       if password_length < 8:
           print("Password length should be at least 8 characters.")
       else:
           break
   except ValueError:
       print("Invalid input. Please enter a number.")

character_sets = []
char_set_choices = input("Include letters? (y/n): ").lower()
if char_set_choices == 'y':
   character_sets.append(letters)

char_set_choices = input("Include numbers? (y/n): ").lower()
if char_set_choices == 'y':
   character_sets.append(numbers)

char_set_choices = input("Include symbols? (y/n): ").lower()
if char_set_choices == 'y':
   character_sets.append(symbols)

if not character_sets:
   print("At least one character set must be selected.")
   exit()

password_characters = ''.join(character_sets)
password = ''.join(random.choice(password_characters) for _ in range(password_length))

print(f"Generated password: {password}")
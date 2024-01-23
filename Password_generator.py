import random
import string

a = "Welcome to Random Password Generator"
print(a.center(50, "-"))

length = int(input("\nPlease enter the required password length: "))

# Define the character sets to use in the password
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

# Combine the character sets into a single string
all_characters = lowercase_letters + uppercase_letters + digits + special_characters

# Generate a random password of length given by user
password = ""
for i in range(length):
  random_pass = random.choice(all_characters)
  password += random_pass

# Printing the random password
print("\nYour Random Password is:", password)

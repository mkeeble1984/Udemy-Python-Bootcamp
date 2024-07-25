import random
import Check_Input
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

password = []

num_letters = (input("How many letters do you want in your password? "))
num_letters = Check_Input.checkNumber(num_letters, "number")

num_numbers = (input("How many numbers do you want in your password? "))
num_numbers = Check_Input.checkNumber(num_numbers, "number")

num_symbols = (input("How many symbols do you want in your password? "))
num_symbols = Check_Input.checkNumber(num_symbols, "number")

for num in range(1, num_letters + 1):
    password.append(random.choice(letters))

for num in range(1, num_numbers + 1):
    password.append(random.choice(nums))

for num in range(1, num_symbols + 1):
    password.append(random.choice(symbols))

random.shuffle(password)
print(f"Your password is: {''.join(password)}")

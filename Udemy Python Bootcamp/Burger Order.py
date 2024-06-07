print("Welcome to Matt's Burger! What's your order?")
size = input(
    "What size burger would you like? Mini (M), Normal (N) or Large (L): ").upper()
add_mushroom = input("Would you like to add mushrooms? ").upper()
extra_cheese = input("Would you like extra cheese? ").upper()

bill = 0

if size == "M":
    bill += 5
    if add_mushroom == "Y":
        bill += 1
if size == "N":
    bill += 8
    if add_mushroom == "Y":
        bill += 1
if size == "L":
    bill += 10
    if add_mushroom == "Y":
        bill += 2
if extra_cheese == "Y":
    bill += 1

print(f"Your fianl bill is: ${bill}.")

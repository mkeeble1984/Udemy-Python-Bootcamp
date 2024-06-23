import random

choice = "Y"

while choice == "Y":
    choice = input("Would you like to flip the coin? ").upper()

    if choice == "Y":
        result = random.randint(0, 1)

        if result == 1:
            print("HEADS")
        else:
            print("TAILS")

import random

while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print(f"Dice 1: {dice1} \nDice 2: {dice2}")

    while True:
        choice = input("Roll the dice again? (Y/N): ").upper()

        if choice == "Y":
            break
        elif choice == "N":
            quit()
        else:
            print("Invalid choice")

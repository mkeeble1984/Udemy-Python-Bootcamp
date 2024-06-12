def checkNumber(userInput):
    while True:
        try:
            userInput = int(userInput)
            break
        except ValueError:
            print("You have not enetered a number.")
            userInput = input("Please enter a number: ")


userInput = input("Please enter a number: ")

checkNumber(userInput)

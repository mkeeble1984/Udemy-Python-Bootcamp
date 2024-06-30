# Function to check if the user has enetered a number, not a word
def checkNumber(userInput):
    while True:
        try:
            userInput = int(userInput)
        except ValueError:
            print("You have not enetered a number.")
            userInput = input("Please enter a number: ")
        else:
            print("Thank you")
            userInput = int(userInput)
            return userInput

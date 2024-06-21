def checkNumber(userInput):  # checks the input to be both a float and less than 1.0
    while True:
        try:
            userInput = float(userInput)
        except ValueError:
            print("You have not enetered a number.")
            userInput = input("Please enter a number: ")
        else:
            if userInput < 1:
                return userInput
            else:
                print("You have not entered a score between 0.0 and 1.0.")
                userInput = input("Enter a score: ")


print("Welcome to The Score Checker. Please enter a score between 0.0 and 1.0.")
new = checkNumber(input("Enter Score: "))

# Pass user input into function, then convert to float if it passes
# userInput = score
# checkNumber(userInput)
print(new)

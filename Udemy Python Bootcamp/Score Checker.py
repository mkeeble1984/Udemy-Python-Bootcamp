def checkNumber(userInput):
    while True:
        try:
            userInput = int(userInput)
            int(userInput) < 10
            break
        except userInput < 10:
            print("Your score is too high.")
            userInput = input("Please enter a score between 0.0 and 1.0")
        except ValueError:
            print("You have not enetered a number.")
            userInput = input("Please enter a number: ")


print("Welcome to The Score Checker. Please enter a score between 0.0 and 1.0.")
score = input("Enter Score: ")

userInput = score
checkNumber(userInput)

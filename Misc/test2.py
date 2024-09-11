# Function to check if the user has enetered a number, not a word
def checkNumber(userInput, var):
    try:
        userInput = int(userInput)
    except ValueError:
        print(f"You have not enetered a {var}.")
        error = True
        return userInput, error
    else:
        userInput = int(userInput)
        error = False
        return userInput, error


input_error = True

while input_error is True:
    user_input = input("Enter a number between 1 and 3, or X: ")

    if user_input == "X" or user_input == "x":
        print("You have entered X")
        input_error = False
    else:
        user_input, input_error = checkNumber(user_input, "number")

        if input_error is True:
            continue
        else:
            if 1 <= user_input <= 3:
                print("valid number between 1 and 3!!!!!!")
                input_error = False
            else:
                print("number is not between 1 and 3.")
                input_error = True

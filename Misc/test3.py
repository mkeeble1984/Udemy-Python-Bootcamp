def checkNumber(userInput, var):
    try:
        userInput = int(userInput)
    except ValueError:
        print(f"\nYou have not enetered a {var}.")
        input_error = True
        return userInput, input_error
    else:
        userInput = int(userInput)
        input_error = False
        return userInput, input_error


def check_user_entry(row_or_col):
    input_error = True

    while input_error is True:
        user_row = input(
            f"\nWhat {row_or_col} is the star on? (1-3, X to quit) ")

        if user_row == "X" or user_row == "x":
            print("Thank you, Maybe we can play again some other time.")
            input_error = False
            guess_again = False
        else:
            user_row, input_error = checkNumber(user_row, "number")

            if input_error is True:
                continue
            else:
                if 1 <= user_row <= 3:
                    print("\nThank you")
                    input_error = False
                    guess_again = True
                else:
                    print("\nThe number must be between 1 and 3.")
                    input_error = True

    return guess_again, user_row


check_user_entry("row")
check_user_entry("column")

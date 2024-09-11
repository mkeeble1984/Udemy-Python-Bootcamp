# function to take in a message and a shift number, then either encode or decode the message.
def convert(p_message, p_shift_num, p_choice):
    new_message = ""
    for i in p_message:
        if i in alphabet:
            if p_choice[0] == "E":
                new_char_pos = (alphabet.index(
                    i) + p_shift_num) % len(alphabet)
                new_message += alphabet[new_char_pos]
            else:
                new_char_pos = (alphabet.index(
                    i) - p_shift_num) % len(alphabet)
                new_message += alphabet[new_char_pos]
        else:
            new_message = new_message + i

    return new_message


# Function to check the value entered for the shift number was an integer.
def checkNumber(userInput):
    while True:
        try:
            userInput = int(userInput)
        except ValueError:
            print("You have not enetered a number.")
            userInput = input(f"Please enter a valid number: ")
        else:
            print("Thank you")
            userInput = int(userInput)
            return userInput


alphabet = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '.', ',', '?', '!', '-', ':', ';', '"', '_', ' ', '<', '>',
            '=', '+', '#', '/', '*', '£', '$', '%', '^', '&', '@', '~', '(', ')']
repeat = "Y"

# Until the user chooses not to play again, they must: enter a message, a shift number and wether to encode or decode.
# The altered message will then be displayed.
while repeat[0] == "Y":
    choice = input("Do you want to encrypt or decrypt your message?\n").upper()
    if choice[0] == "E" or choice[0] == "D":
        message = input("Enter your message:\n")
        shift_number = input("Enter the shift number:\n")
        shift_number = checkNumber(shift_number)
        new_message = convert(message, shift_number, choice)
        print(
            f"The {'encoded' if choice[0] == 'E' else 'decoded'} message is: {new_message}")
        repeat = input("Do you want to convert another message?\n").upper()
    else:
        print("Dumb Ass!!!! You need to choose either ENCRYPT or DECRYPT!!!")

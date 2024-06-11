def checkNumber(userInput, number):
    while number is False:
        print("You have not enetered a number.")
        userInput = input("Please enter a number: ")
        if userInput.isdigit():
            number = True
            print("Thank You!!!!!!!!!!")
        else:
            continue


userInput = input("Please enter a number: ")
number = False
if userInput.isdigit():
    print("Thank You!!")
else:
    checkNumber(userInput, number)

def checkNumber(userInput):
    while True:
        try:
            userInput = float(userInput)
            break
        except ValueError:
            print("You have not enetered a number.")
            userInput = input("Please enter a number: ")


hours = input("Enter Hours: ")
userInput = hours
checkNumber(userInput)
hours = float(userInput)

rate = input("Enter Rate: £")
userInput = rate
checkNumber(userInput)
rate = float(userInput)

if hours > 40:
    overtime = hours - 40
    pay = 40 * rate + overtime * rate * 1.5
else:
    pay = hours * rate
print("Pay: £", round(pay, 2))

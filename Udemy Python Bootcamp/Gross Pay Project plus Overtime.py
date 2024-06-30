import Check_Input

# Takes in the number of hours worked then checks it to be a number, not a word. Then converts it to a float.
hours = input("Enter Hours: ")
userInput = hours
hours = float(Check_Input.checkNumber(userInput))

# Takes in the hpurly rate then checks it to be a number, not a word. Then converts it to a float.
rate = input("Enter Rate: £")
userInput = rate
rate = float(Check_Input.checkNumber(userInput))


def compute_pay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        pay = 40 * rate + overtime * rate * 1.5
    else:
        pay = hours * rate

    return format(pay, ".2f")


# Calculates the pay based on the hours worked and the hourly rate, then prints to the display.
print(f"Pay: £{compute_pay(hours, rate)}")

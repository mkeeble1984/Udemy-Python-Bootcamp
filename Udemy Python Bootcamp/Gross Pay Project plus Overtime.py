try:
    hours = float(input("Enter Hours: "))
except:
    print("You did not enter a valid number. Please try again.")
    hours = float(input("Enter Hours: "))
try:
    rate = float(input("Enter Rate: £"))
except:
    print("You did not enter a valid number. Please try again.")
    rate = float(input("Enter Rate: £"))
if hours > 40:
    overtime = hours - 40
    pay = 40 * rate + overtime * rate * 1.5
else:
    pay = hours * rate
print("Pay: £", round(pay, 2))

try:
    year = int(input("Please enter a year: "))
except:
    print("You have not entered a valid year. Please make sure it is only numbers.")
    year = int(input("Please enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} IS a leap year.")
        else:
            print(
                f"The year {year} IS NOT a leap year. [Not divisible by 400]")
    else:
        print(f"The year {year} IS a leap year.")
else:
    print(f"The year {year} IS NOT a leap year. [Not divisible by 4]")

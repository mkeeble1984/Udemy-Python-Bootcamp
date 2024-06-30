import Check_Input


def leapYearCheck(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f"The year {year} IS a leap year."
            else:
                return f"The year {year} IS NOT a leap year. [Not divisible by 400]"
        else:
            return f"The year {year} IS a leap year."
    else:
        return f"The year {year} IS NOT a leap year. [Not divisible by 4]"


# Take in users chosen year, then pass it through a checker to see if it is a number, not text.
year = (input("Please enter a year: "))
year = Check_Input.checkNumber(year)
# If it passes, it will be returned as an integer before being checked to see if it is a leap year.
print(leapYearCheck(year))

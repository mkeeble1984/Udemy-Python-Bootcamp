import Check_Input

temp = input("Please enter a temperature: ")

temp = Check_Input.checkNumber(temp, "temperature")


def Check_Temp(temp):
    if temp >= 28:
        return "The temperature is HOT."
    elif temp >= 18:
        return "The temperature is WARM."
    else:
        return "The temperature is COLD."


print(Check_Temp(temp))

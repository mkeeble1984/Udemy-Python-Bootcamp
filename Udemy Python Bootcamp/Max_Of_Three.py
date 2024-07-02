import Check_Input

num_1 = input("Please enter the first number: ")
num_1 = Check_Input.checkNumber(num_1, "number")

num_2 = input("Please enter the second number: ")
num_2 = Check_Input.checkNumber(num_2, "number")

num_3 = input("Please enter the third number: ")
num_3 = Check_Input.checkNumber(num_3, "number")

num_list = num_1, num_2, num_3
print(f"The largest number you have entered is {max(num_list)}.")

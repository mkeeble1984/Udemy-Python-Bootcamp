def input_check(user_input):
    while user_input != "done":
        try:
            user_input = int(user_input)
        except ValueError:
            if user_input == "done":
                pass
            else:
                print("Error, please enter numeric input")
        else:
            print("Thank you")
            # print(user_input)
            # print(type(user_input))
        return user_input


count = 0
user_input = ""
while user_input != "done":
    user_input = input("Enter a number: ")
    num = input_check(user_input)
    count = count + num
    print(count)

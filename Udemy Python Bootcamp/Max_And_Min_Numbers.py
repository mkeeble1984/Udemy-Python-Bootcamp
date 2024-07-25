def input_check(user_input):
    try:
        number = float(user_input)
        return number
    except (ValueError, TypeError):
        print("Error, please eneter a numeric input")
        return False


num_list = []

while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break

    number = input_check(user_input)
    if not number:
        continue

    num_list.append(number)
    num_list.sort()

print(f"Maximum number: {num_list[-1]}, Minimum number: {num_list[0]}")

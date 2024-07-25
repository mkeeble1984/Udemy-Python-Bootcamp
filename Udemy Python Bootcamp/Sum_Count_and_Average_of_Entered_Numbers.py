def input_check(user_input):
    try:
        num = float(user_input)
        return num
    except (ValueError, TypeError):
        print("Error, please eneter a numeric input")
        return False


count = 0
total = 0.0
average = 0.0

while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break

    number = input_check(user_input)
    if not number:
        continue

    count += 1
    total += number
if count != 0:
    avergae = total / count
print(total, count, average)

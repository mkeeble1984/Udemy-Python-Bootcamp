def factorial(p_num):
    for x in range(1, p_num):
        p_num *= x
    if p_num == 0:
        p_num = 1
    return p_num


p_num = int(input("Please enter a number: "))
if p_num < 0:
    print("Factorial does not exist for negative numbers")
else:
    factorial(p_num)
    print(f"The factorial of {p_num} is {factorial(p_num)}")

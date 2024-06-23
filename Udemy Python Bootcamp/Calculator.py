first = int(input("What is the first number? "))
second = int(input("What is the second number?"))
opperation = input("Pick operation from this list (+,-,*,/)")

if opperation == "+":
    calculation = first + second
elif opperation == "-":
    calculation = first - second
elif opperation == "*":
    calculation = first * second
elif opperation == "/":
    calculation = first / second

print(f"{first} {opperation} {second} = {calculation}")

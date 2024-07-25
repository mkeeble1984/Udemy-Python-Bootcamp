import time
num = 1
for num in range(1, 101):
    if num % 5 == 0 and num % 7 == 0:
        print("Fizz Buzz")
    elif num % 5 == 0:
        print("Fizz")
    elif num % 7 == 0:
        print("Buzz")
    else:
        print(num)
    time.sleep(0.5)

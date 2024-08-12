def print_pattern(n):
    stars = "* "
    for i in range(n):
        print(stars)
        stars = stars + "* "

    stars = stars[:-2]
    for i in range(n, 1, -1):
        stars = stars[:-2]
        print(stars)


n = int(input("Please enter a number: "))
print_pattern(n)

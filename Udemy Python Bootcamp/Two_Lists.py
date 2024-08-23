list_one = [4, 12, 16, 21, 24, 28, 32]
list_two = [5, 10, 15, 20, 25, 30, 35]
# list_three = []

list_three = list_one[1::2] + list_two[::2]

print(list_three)

import random

names = input("Enter everyone's names, separated by a comma (,): ")
names = names.split(", ")

rand_num = random.randint(0, len(names)-1)

print(f"{names[rand_num]} has been chosen to pay the bill!!!!!!")

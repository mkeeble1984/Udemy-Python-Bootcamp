import math


def area_of_wall(height, width):
    area = height * width
    return area


def num_of_cans(area):
    cans = area / 4
    return cans


height = int(input("What is the height of the wall? "))
width = int(input("What is the width of the wall? "))

area_of_wall(height, width)
area = (area_of_wall(height, width))
num_of_cans(area)
cans = num_of_cans(area)

cans = math.ceil(cans)

print(f"You will need {cans} cans of paint.")

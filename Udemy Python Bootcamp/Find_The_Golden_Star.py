import random


def print_map(p_map):
    print('\n'.join([' '.join(['{:2}'.format(item)
          for item in row]) for row in p_map]))


map1 = [["⬜️", "️⬜️", "️⬜️"], ["⬜️", "️⬜️", "️⬜️"], ["⬜️", "️⬜️", "️⬜️"]]
print("This is our initial map...")
print_map(map1)

print("A GOLDEN STAR is hidden somewhere in the map. Where do you think it is?\n")
user_row = int(input("What row is the star on? (1-3) ")) - 1
user_col = int(input("What column is the star on? (1-3) ")) - 1
rand_row = random.randint(0, 2)
rand_col = random.randint(0, 2)
map1[rand_row][rand_col] = "⭐"


if user_row == rand_row and user_col == rand_col:
    print("\nCongratulations!!! You have found the Golden STAR!")
    print_map(map1)

else:
    print("\nUnfortunatly you couldn't find it 🙁")
    map1[user_row][user_col] = "💩"
    print_map(map1)

input()

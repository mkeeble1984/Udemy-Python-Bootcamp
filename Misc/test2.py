import time
import os

LOGO = r"""
 /$$$$$$$                                             /$$                 /$$ /$$
| $$__  $$                                           | $$                | $$| $$
| $$  \ $$ /$$$$$$  /$$  /$$  /$$  /$$$$$$   /$$$$$$ | $$$$$$$   /$$$$$$ | $$| $$
| $$$$$$$//$$__  $$| $$ | $$ | $$ /$$__  $$ /$$__  $$| $$__  $$ |____  $$| $$| $$
| $$____/| $$  \ $$| $$ | $$ | $$| $$$$$$$$| $$  \__/| $$  \ $$  /$$$$$$$| $$| $$
| $$     | $$  | $$| $$ | $$ | $$| $$_____/| $$      | $$  | $$ /$$__  $$| $$| $$
| $$     |  $$$$$$/|  $$$$$/$$$$/|  $$$$$$$| $$      | $$$$$$$/|  $$$$$$$| $$| $$
|__/      \______/  \_____/\___/  \_______/|__/      |_______/  \_______/|__/|__/
                                                                                
"""


def five_nums(p_split_nums):
    """Function to check the user has eneterd 5 numbers"""
    if len(p_split_nums) != 5:
        print("\nERROR - You have not selected 5 numbers, please try again.")
        time.sleep(2.5)
        os.system("cls")
        return False


while True:
    print(LOGO)
    print()
    print("Select 5 numbers from 1 - 69, with a space in between (e.g. 1 5 9 22 51)")
    player_nums = input("--> ")

    split_nums = player_nums.split()
    five_nums(split_nums)

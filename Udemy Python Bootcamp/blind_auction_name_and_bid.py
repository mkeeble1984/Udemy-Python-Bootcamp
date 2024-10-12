"""Takes in the users name and bid, then adds it to the dictionary."""
import Check_Input


def name_and_bid(blind_auction_dict):
    """Function to add user name and bid to dictionary"""
    user_name = input("What is your name?: ")

    input_correct = False
    while input_correct is False:
        user_bid = input("What is your bid?: £")

        user_bid, input_correct = Check_Input.checkNumber(
            user_bid, input_correct)

    blind_auction_dict[user_name] = user_bid

    return blind_auction_dict

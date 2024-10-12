"""Main Program"""
import Blind_Auction_Logo
import blind_auction_name_and_bid
import blind_auction_highest_bid
import os

blind_auction_dict = {}

OTHER_BIDDERS = True
while OTHER_BIDDERS is True:
    Blind_Auction_Logo.blind_auction_logo()
    blind_auction_dict = blind_auction_name_and_bid.name_and_bid(
        blind_auction_dict)

    new_bid = input("Are there any other bidders? (Y/N): ").upper()
    while True:
        if new_bid == "Y" or new_bid == "N":
            break
        else:
            print("\nYOUR INPUT IS INCORRECT - PLEASE SELECT EITHER 'Y' OR 'N'.\n")
            new_bid = input("Are there any other bidders? (Y/N): ").upper()

    if new_bid == "Y":
        OTHER_BIDDERS = True
        os.system('cls')
    else:
        OTHER_BIDDERS = False

high_bidder, high_bid = blind_auction_highest_bid.highest_bid(
    blind_auction_dict)
os.system('cls')
Blind_Auction_Logo.blind_auction_logo()
print(f"\nThe highest bidder was {high_bidder} with a bid of £{high_bid}.")

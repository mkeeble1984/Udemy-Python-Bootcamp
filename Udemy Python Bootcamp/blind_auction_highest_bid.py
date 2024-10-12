"""Takes in a dictionary and selects the highest value."""


def highest_bid(blind_auction_dict):
    """Takes in a dictionary, sorts it by 'bid', then returns highest bidder."""
    sorted_dict = dict(sorted(blind_auction_dict.items(), key=lambda x: x[1]))

    high_bidder = list(sorted_dict)[-1]
    high_bid = sorted_dict[high_bidder]

    return high_bidder, high_bid

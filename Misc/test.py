blind_auction_dict = {'matt': 5, 'Thea': 1, 'Emma': 9}

print(blind_auction_dict)
new_blind = dict(sorted(blind_auction_dict.items(), key=lambda x: x[1]))
print(new_blind)
last = list(new_blind)[-1]
bid = new_blind[last]
print(last)
print(bid)

dict1 = {'One': 2, 'Two': 2, 'Three': 3}
dict2 = {'Three': 3, 'Four': 4, 'Five': 5}

# Function to combined two dictionaries together


def merge_dict(p_dict1, p_dict2):
    new_dict = dict(p_dict1)
    new_dict |= p_dict2
    return new_dict


print(merge_dict(dict1, dict2))

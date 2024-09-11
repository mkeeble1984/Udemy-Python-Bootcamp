import pprint

custom_dict = {
    "name": "Elshad",
    "age": None,
    "city": "London"
}

# Function to remove any empty items from a dictionary


def remove_empty_items(p_custom_dict):
    new_dict = {}
    for key, value in p_custom_dict.items():
        if value is not None:
            new_dict[key] = value
    return new_dict


pprint.pp(remove_empty_items(custom_dict))

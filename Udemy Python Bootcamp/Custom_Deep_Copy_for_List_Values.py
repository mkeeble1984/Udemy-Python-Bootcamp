import copy
import pprint

original_dict = {
    "names": ["Elshad", "John", "Edy"],
    "numbers": [1, 2, 3, 4, 5]
}


def deep_copy(p_dict):
    new_dict = {}
    for key, value in p_dict.items():
        new_value = value.copy()
        new_dict[key] = new_value
    return new_dict


copied_dict = deep_copy(original_dict)
copied_dict["names"].append("Jack")
copied_dict["numbers"].append(6)

pprint.pp(original_dict, width=50)
pprint.pp(copied_dict, width=50)

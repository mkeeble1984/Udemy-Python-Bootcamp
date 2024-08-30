import pprint
custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]


def group_types(p_custom_list):
    new_dict = dict.fromkeys(p_custom_list)
    for key in p_custom_list:
        if isinstance(key, str):
            new_dict[key] = "String"
        else:
            new_dict[key] = "Integer"
    return new_dict


pprint.pp(group_types(custom_list))

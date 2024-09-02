dict1 = {1: "one", 2: "two"}
dict2 = {3: "three", 4: "four"}
dict3 = {5: "five", 6: "six"}


def concatenate(p_dict1, p_dict2, p_dict3):
    new_dict = {}
    new_dict.update(p_dict1)
    new_dict.update(p_dict2)
    new_dict.update(p_dict3)
    # new_dict = {**p_dict1, **p_dict2, **p_dict3}
    return new_dict


print(concatenate(dict1, dict2, dict3))

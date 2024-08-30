def value_length(p_dict):
    new_dict = {}
    for key, value in p_dict.items():
        new_dict[key] = {value: len(value)}
    return new_dict


names_dict = {
    1: "Elshad",
    2: "Renad",
    3: "Johanna",
    4: "Appmillers"
}
print(value_length(names_dict))

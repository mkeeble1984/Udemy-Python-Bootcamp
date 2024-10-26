def even_index_items(p_my_tuple):
    new_tuple = tuple(p_my_tuple[i] for i in range(0, len(p_my_tuple), 2))
    return new_tuple


my_tuple = ("a", "b", "c", "d", "e", "f", "g")

print(even_index_items(my_tuple))

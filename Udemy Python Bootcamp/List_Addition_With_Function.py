def custom_insert(list, value):
    list2 = list[:]
    list2.append(value)
    return list2


list1 = [1, 2, 3, 4, 5]
list2 = custom_insert(list1, 6)
print(list1)
print(list2)

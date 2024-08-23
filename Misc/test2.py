def concatenate(list1, list2):
    new_list = []
    for i in list1:
        for y in list2:
            new_list.append(i + y)
    print(new_list)


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concatenate(list1, list2)

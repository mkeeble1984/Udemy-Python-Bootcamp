def count_words(p_list):
    count = 0
    for item in p_list:
        if item[0] == item[-1]:
            count += 1
    print(count)


list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']

count_words(list1)

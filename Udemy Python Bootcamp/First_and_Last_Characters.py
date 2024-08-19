def count_words(p_list):
    count = 0
    for item in p_list:
        first = item[0]
        last = item[-1]
        if first == last:
            count = count + 1
    print(count)


list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']

count_words(list1)

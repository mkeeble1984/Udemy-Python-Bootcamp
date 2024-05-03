def copy_sort(array):
    copy = array[:]
    sorted_copy = []
    # Algorithm sequence to be added here.

    while len(copy) > 0:
        minimum = 0
        for element in range(0, len(copy)):
            if copy[element] < copy[minimum]:
                minimum = element
        print('\tRemoving', copy[minimum], 'from', copy)
        sorted_copy.append(copy.pop(minimum))

    return sorted_copy


array = [5, 3, 1, 2, 6, 4]
print('Copy Sort...')
print('Array :', array)

print('Copy :', copy_sort(array))
print('Array :', array)

sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]

length = len(sample_list)
third = int(length / 3)
chunk1 = sample_list[:third]
chunk2 = sample_list[third:third*2]
chunk3 = sample_list[third*2:]

print(list(reversed(chunk1)))
print(list(reversed(chunk2)))
print(list(reversed(chunk3)))

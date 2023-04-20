'''8. wap to print all distinct values present in a dict.'''
list1 = []
dict1 = {'key1': 2, 'key2': 5, 'key3': 10, 'key4': 3, 'key5': 13, 'key12': 13, 'key6': 4, 'key7': 10, 'key8': 4, 'key9': 2, 'key10': 34, 'key11': 11}
for key in dict1:
    if dict1[key] not in list1:
        list1.append(dict1[key])
print(list1)
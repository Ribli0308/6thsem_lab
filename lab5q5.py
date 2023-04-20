'''5. wap to mult all the elements present in a dictionary.'''
dictionary = {'key1': 2, 'key2': 5, 'key3': 10, 'key4': 3, 'key5': 13, 'key6': 9}
product = 1
for key in dictionary:
    product *= dictionary[key]
print("product of all values in dictionary is", product)
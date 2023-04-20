'''9. wap to convert a dict into a list of lists.'''
'''dict1 = {'key1': 2, 'key2': 5, 'key3': 10, 'key4': 3, 'key5': 13, 'key12': 9}
list1 = []
for elem in dict1:
    key, value = elem, dict1[elem]
    list1.append([key, value])
print(list1)'''
def func(**a):
    print(a["name"])

func(roll = 104, name = "abc")
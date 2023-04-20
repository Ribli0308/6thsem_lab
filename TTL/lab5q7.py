'''7. wap to sort a given dict by its key.'''
dict1  = {11: 'a', 7: 'b', 13: 'c', 1: 'd', 34: 'e', 17: 'f'}
print(dict1)
listkey = list(dict1.keys())
for i in range(len(listkey)-1):  
    for j in range(len(listkey)-1):  
        if listkey[j]>listkey[j+1]:  
            listkey[j], listkey[j + 1] = listkey[j + 1], listkey[j]
newDict = {i: dict1[i] for i in listkey}
print(newDict)
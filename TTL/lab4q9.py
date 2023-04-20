'''wap to find out mult of all the nums in a given tuple.'''
list1 = [34, 10, 23, 11, 3, 2]
mult = 1
print(list1)
for elem in list1:
    mult *= elem
print('product: ', mult)
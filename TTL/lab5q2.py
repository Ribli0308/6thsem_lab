'''2. wap to perform union, intersection, set difference on two sets.'''
set1 = {11, 34, 56, 98, 20}
set2 = {33, 17, 67, 34, 56, 44, 14}
set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5 = set1.difference(set2)
set6 = set2.difference(set1)
print("Union ", set3)
print("intersection ", set4)
print("difference set1 - set2 ", set5)
print("difference set2 - set1 ", set6)
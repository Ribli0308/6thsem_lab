'''WAP to remove duplicates from a list.'''
lst = [1, 2, 3, 1, 4, 3, 7, 9, 4, 4, 5, 6, 7, 9, 8, 8, 8, 3]
newlst = []
for elem in lst:
    if elem not in newlst:
        newlst.append(elem)
print("after removing duplicates :", newlst)
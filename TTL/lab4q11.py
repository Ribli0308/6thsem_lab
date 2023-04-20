'''wap to check the freq of a specific elem within a tuple.'''
tuple1 = (1, 2, 3, 4, 1, 3, 7, 7, 8, 10, 2, 4, 4)
count = 0
print(tuple1)
for elem in tuple1:
    if elem == 4:
        count += 1
print("frequency of 4: ", count)
'''wap to convert a tuple of strings to int values.'''
tuple1 = ('1', '2', '3', '4', '5')
print(tuple1)
tuple2 = [int(x) for x in tuple1]
tuple2 = tuple(tuple2)
print(tuple2)
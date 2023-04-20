'''8. wap to enter three strings and try to delete one of the strings, also check the type of the strings and the address of the strings.[id(string)]'''
s1 = input("Enter string1: ")
s2 = input("Enter string2: ")
s3 = input("Enter string3: ")
print("s1 is ", type(s1))
print("s2 is ", type(s2))
print("s3 is ", type(s3))
print("s1 address ", id(s1))
print("s2 address ", id(s2))
print("s3 address ", id(s3))
del s2
print("s2 is deleted")
print("s2 address: ", id(s2))
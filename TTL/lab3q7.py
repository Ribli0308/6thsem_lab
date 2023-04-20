'''7. wap to check a particular substring is availbale within a string or not, also print the given string as it is.'''
ms = input("enter main string ")
ss = input("Enter substring ")
if ss in ms:
    print("It is a substring")
else:
    print("It is not a substring")
print("mainString: ", ms)
print("subString: ", ss)

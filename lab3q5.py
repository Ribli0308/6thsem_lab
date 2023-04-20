'''5. wap to retrive the substring of a string.'''
string = input("Enter a string")
print("The substrings are: ")
for i in range(2):
    for j in range(3, 5):
        print(string[i:j])

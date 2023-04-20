"""4. wap to check the given string is palindrome or not."""
string = input("Enter a string ")
reverseString = string[:: -1]
print("is the given string palindrome? ", string == reverseString)
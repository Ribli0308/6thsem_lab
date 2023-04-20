def checkpalindrome(num):
    newNum = num[:-1]
    return num == newNum

y = input("Enter number")
print("Is the given number palindrome? ", checkpalindrome(y))

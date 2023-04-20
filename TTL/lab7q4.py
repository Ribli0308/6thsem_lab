#4. wap class to reverse a string word by word.
class String:
    def reverseString(self, string):
        txt = string.split()[::-1]
        return ' '.join([word for word in txt])
string = String()
print(string.reverseString('Hello World'))
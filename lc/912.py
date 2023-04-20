def decodings(string):
    if len(string) == 0 or (len(string) == 1 and string[0] == '0'):
        return 0
    return numDecoder(string, len(string))

def numDecoder(string, n):
    if n == 0 or n == 1:
        return 1
    count = 0
    if string[n - 1] > '0':
        count = numDecoder(string, n - 1)
    if string[n - 2] == '1' or (string[n - 2] == '2' and string[n - 1] < '7'):
        count += numDecoder(string, n - 2)
    return count

digits = "1126"
print("Count is ", decodings(digits))
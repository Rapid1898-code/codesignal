def buildPalindrome(st):
    # if st == st[::-1]:
    #     return st
    for i in range(100):
        checkString = st + st[:i][::-1]
        if checkString == checkString[::-1]:
            return checkString

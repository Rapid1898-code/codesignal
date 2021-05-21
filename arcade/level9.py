def allLongestStrings(inputArray):
    maxLen = 0
    ergList = []
    for i in inputArray:
        if len(i) > maxLen:
            maxLen = len(i)
    for i in inputArray:
        if len(i) == maxLen:
            ergList.append(i)
    return ergList
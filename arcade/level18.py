def palindromeRearranging(inputString):
    charsDict = {}
    for c in inputString:
        if c not in charsDict:
            charsDict[c] = 1
        else:
            charsDict[c] += 1
    countNotEqual = 0
    for key, val in charsDict.items():            
        if val % 2 != 0:
            countNotEqual += 1
            if countNotEqual > 1:
                return False
    return True
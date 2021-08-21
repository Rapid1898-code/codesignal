def differentSymbolsNaive(s):
    exitChars = []
    countDifferentChars = 0
    for char in s:
        if char not in exitChars:
            countDifferentChars +=1
            exitChars.append(char)
    return countDifferentChars
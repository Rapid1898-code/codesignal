def isBeautifulString(inputString):
    charCount = {"a":-1,"b":-1,"c":-1}
    for char in inputString:
        if char not in charCount or charCount[char] == -1:
            charCount[char] = 1
        else:
            charCount[char] += 1   

    sortedCharCount = dict(sorted(charCount.items()))
    print(sortedCharCount)
    
    actCount = False
    for k,v in sortedCharCount.items():
        print(actCount,v)
        if actCount != False:
            print("Drinn")
            if v > actCount:
                print("Drinnen!")
                return False
            else:
                actCount = v
        else:
            actCount = v            
    return True
            
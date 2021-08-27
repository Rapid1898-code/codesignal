def deleteDigit(n):
    maxNum = 0
    checkN = str(n)
    for i in range(len(checkN)):
        
        print(i)
        
        checkNum = checkN[:i] + checkN[i+1:] 
        
        print(checkNum)
        
        if int(checkNum) > maxNum:
            maxNum = int(checkNum)
    return maxNum


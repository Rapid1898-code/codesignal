def bishopAndPawn(bishop, pawn):
    charNum = ord(bishop[0]) - 96   
    num = bishop[1]
    bishopFields = []
    
    tmpNum1 = charNum
    tmpNum2 = int(num)
    while True:
        tmpNum1 -= 1
        tmpNum2 += 1
        if tmpNum1 == 0:
            break
        bishopFields.append(chr(tmpNum1 + 96) + str(tmpNum2))
        
    tmpNum1 = charNum
    tmpNum2 = int(num)
    while True:
        tmpNum1 -= 1
        tmpNum2 -= 1
        if tmpNum1 == 0:
            break
        bishopFields.append(chr(tmpNum1 + 96) + str(tmpNum2))
        
    tmpNum1 = charNum
    tmpNum2 = int(num)
    while True:
        tmpNum1 += 1
        tmpNum2 += 1
        if tmpNum1 == 9:
            break
        bishopFields.append(chr(tmpNum1 + 96) + str(tmpNum2))
        
    tmpNum1 = charNum
    tmpNum2 = int(num)
    while True:
        tmpNum1 += 1
        tmpNum2 -= 1
        if tmpNum1 == 9:
            break
        bishopFields.append(chr(tmpNum1 + 96) + str(tmpNum2))
    
    if pawn in bishopFields:
        return True
    else:
        return False
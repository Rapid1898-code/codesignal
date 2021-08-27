def chessKnight(cell):
    countPossible = 0
    char = ord(cell[0])-96
    num = int(cell[-1])
    
    print(char)
    
    for i in [2,-2]:
        for j in [1,-1]:
            tmpchar = char + i
            tmpnum = num + j
            
            print(tmpchar, tmpnum)
            
            if tmpchar >= 1 and tmpchar <=8 and tmpnum >= 1 and tmpnum <=8:
                countPossible += 1
    for i in [2,-2]:
        for j in [1,-1]:
            tmpnum = num + i
            tmpchar = char + j
            
            print(tmpchar, tmpnum)
            
            if tmpchar >= 1 and tmpchar <=8 and tmpnum >= 1 and tmpnum <=8:
                countPossible += 1
    return countPossible
    


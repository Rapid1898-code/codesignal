def digitDegree(n):
    countRounds = 0
    while len(str(n)) > 1:
        tmpNum = 0
        for c in str(n):
            tmpNum += int(c)
        n = tmpNum
        countRounds += 1
    return countRounds
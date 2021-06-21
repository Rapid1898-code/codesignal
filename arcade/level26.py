def evenDigitsOnly(n):
    tmpStr = str(n)
    for elem in tmpStr:
        if int(elem) % 2 != 0:
            return(False)
    return(True)
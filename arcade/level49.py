def lineEncoding(s):
    actChar = False
    countChar = False
    ergString = ""
    for char in s:
        if actChar == False:
            actChar = char
            countChar = 1
        else:
            if actChar != char:
                if countChar > 1:
                    ergString = ergString + str(countChar) + actChar
                else:
                    ergString = ergString + actChar
                actChar = char
                countChar = 1
            else:
                countChar += 1
    if countChar == 1:
        ergString = ergString + actChar
    else:
        ergString = ergString + str(countChar) + actChar
        
    return ergString
def isIPv4Address(inputString):
    tmpParts = inputString.split(".")
    if len(tmpParts) != 4:
        return False
    print(tmpParts)
    for i,e in enumerate(tmpParts):                
        if e in ["","00","01"]:
            return False
        try:
            int(e)
        except:
            return False
        if int(e) > 255:
            return False
        # if i in [1,2] and int(e) < 1:
        #     return False
        # if i == 3 and len(e) > 1:
        #     return False
    return True

def isMAC48Address(inputString):
    seperateElems = inputString.split("-")
    if len(seperateElems) != 6:
        return False
    else:
        print(seperateElems)
        for e in seperateElems:
            if len(e) != 2:
                return False
            for c in e:
                if c not in ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]:
                    return False
        return True

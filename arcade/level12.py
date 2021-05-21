def sortByHeight(a):
    boolList = []
    heightList = []
    for i in a:
        if i == -1:
            boolList.append(False)
        else:
            boolList.append(True)
            heightList.append(i)
    heightList.sort()
    idx = 0
    for idxBool, BoolElem in enumerate(boolList):
        if BoolElem == True:
            a[idxBool] = heightList[idx]
            idx += 1
    return a
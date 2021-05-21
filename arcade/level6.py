def makeArrayConsecutive2(statues):
    countAdded = 0
    statues.sort()
    maxElem = max(statues)
    minElem = min(statues)
    for i in range(minElem,maxElem,1):
        if i not in statues:
            countAdded += 1
    return(countAdded)
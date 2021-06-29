def absoluteValuesSumMinimization(a):   
    minDiff = 999999999
    ergElem = False
    for e in a:
        tmpDiff = 0
        for f in a:
            tmpDiff += abs(f - e)
        if tmpDiff < minDiff:
            minDiff = tmpDiff
            ergElem = e
        elif tmpDiff == minDiff and e < ergElem:
            ergElem = e
    return (ergElem)   
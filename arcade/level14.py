def alternatingSums(a):
    firstList = []
    secondList = []
    ergList = []
    for i, e in enumerate(a):
        if i % 2 == 0:
            firstList.append(e)
        else:
            secondList.append(e)            
    ergList.append(sum(firstList))
    ergList.append(sum(secondList))
    return ergList
def extractEachKth(inputArray, k):
    ergArray = []
    for idx,elem in enumerate(inputArray):
        if (idx+1) % k != 0:
            ergArray.append(elem)
    return ergArray
def arrayMaximalAdjacentDifference(inputArray):
    maxDiff = 0
    for i,e in enumerate(inputArray):
        if i == 0:
            continue
        if abs(e - inputArray[i-1]) > maxDiff:
            maxDiff = abs(e - inputArray[i-1])
    return maxDiff
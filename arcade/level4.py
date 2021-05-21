def adjacentElementsProduct(inputArray):
    maxProduct = -99999999999999999
    for idx, elem in enumerate(inputArray):
        if idx == 0:
            continue
        if elem * inputArray[idx-1] > maxProduct:
            maxProduct = elem * inputArray[idx-1]
    return maxProduct
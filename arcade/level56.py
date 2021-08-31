def digitsProduct(product):
    if product == 1:
        return 1
    if product == 0:
        return 10
    for i in range(10000):
        if len(str(i)) < len(str(product)):
            continue
        tmpProduct = 1
        for c in (str(i)):
            tmpProduct *= int(c)
        if tmpProduct == product:
            return i        
    return -1
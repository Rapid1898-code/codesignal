def isLucky(n):
    n = str(n)
    middle = int(len(n)/2)
        
    firstPart = n[:middle]
    secondPart = n[middle:]
    
    sum1 = sum2 = 0
    for i in firstPart:
        sum1 += int(i)
    for i in secondPart:
        sum2 += int(i)
        
    if sum1 == sum2:
        return True
    else:
        return False
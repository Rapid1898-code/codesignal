def avoidObstacles(inputArray):
    for i in range(2,10000):
        for i2 in range(0,10000,i):
            if i2 > max(inputArray):
                return (i)
            if i2 in inputArray:
                break
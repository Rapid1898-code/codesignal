<<<<<<< HEAD
def avoidObstacles(inputArray):
    for i in range(2,10000):
        for i2 in range(0,10000,i):
            if i2 > max(inputArray):
                return (i)
            if i2 in inputArray:
                break
=======
def boxBlur(image):
    workonCenterX = len(image[0]) - 2
    workonCenterY = len(image) - 2
    
    erg = []
    for y in range(workonCenterY):
        tmpYList = []
        for x in range(workonCenterX):
            
            # print(image)
            # print(f"X: {x}")
            # print(f"Y: {y}")
            
            sum  = image[y][x] + image[y][x+1] + image[y][x+2] + \
                    image[y+1][x] + image[y+1][x+1] + image[y+1][x+2] + \
                    image[y+2][x] + image[y+2][x+1] + image[y+2][x+2]
            tmpYList.append(sum // 9)
        erg.append(tmpYList)
    return(erg)  
>>>>>>> 32d3f2ae48d7970a86679d9ede71d33b8360a88e

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
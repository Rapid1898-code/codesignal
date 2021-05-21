def shapeArea(n):
    squares = 1
    for i in range(2,n+1,1):
        squares += (i*2) + (2*(i-2))
    return squares    
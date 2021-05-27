def minesweeper(matrix):
    ergMatrix = []
    for y in range(len(matrix)):
        tmpRow = []
        for x in range(len(matrix[0])):
            countBombs = 0
            
            if x-1 >= 0 and y-1 >=0 and matrix[y-1][x-1]:
                countBombs += 1
            if y-1 >= 0 and matrix[y-1][x]:
                countBombs += 1            
            if y-1 >= 0 and x+1 < len(matrix[0]) and matrix[y-1][x+1]:
                countBombs += 1
                
            if x-1 >= 0 and matrix[y][x-1]:
                countBombs += 1
            if x+1 < len(matrix[0]) and matrix[y][x+1]:
                countBombs += 1            
            if x-1 >= 0 and y+1 < len(matrix) and matrix[y+1][x-1]:
                countBombs += 1
            if y+1 < len(matrix) and matrix[y+1][x]:
                countBombs += 1            
            if x+1 < len(matrix[0]) and y+1 < len(matrix) and matrix[y+1][x+1]:            
                countBombs += 1
            tmpRow.append(countBombs)
        ergMatrix.append(tmpRow)
    return(ergMatrix)
            
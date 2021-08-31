def differentSquares(matrix):
    existSquares = []
    for i in range(len(matrix[0]) - 1):
        for j in range(len(matrix) - 1):
            tmpSquare = [matrix[j][i], matrix[j][i + 1], matrix[j + 1][i], matrix[j + 1][i + 1]]
            if tmpSquare not in existSquares:
                existSquares.append(tmpSquare)
    return len(existSquares)
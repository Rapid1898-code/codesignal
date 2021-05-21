def matrixElementsSum(matrix):
    countSum = 0
    blockedRoomIDX = []
    for idxFloor, floor in enumerate(matrix):
        for idxRoom, room in enumerate(floor):
            if room == 0:
                blockedRoomIDX.append(idxRoom)
            else:
                if idxRoom not in blockedRoomIDX:                    
                    countSum += room
    return countSum
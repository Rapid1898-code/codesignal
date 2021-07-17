def growingPlant(upSpeed, downSpeed, desiredHeight):
    countDays = 0
    sizePlant = 0
    while True:                
        countDays += 1    
        sizePlant += upSpeed
        if sizePlant >= desiredHeight:
            break
        sizePlant -= downSpeed    
        
    return countDays
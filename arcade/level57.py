def fileNaming(names):
    resultList = []
    for name in names:                               
        if name not in resultList:            
            resultList.append(name)
        else:
            for i in range (1,100):
                if f"{name}({i})" not in resultList:
                    resultList.append(f"{name}({i})")
                    break                                                              
    return resultList
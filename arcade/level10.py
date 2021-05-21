def commonCharacterCount(s1, s2):
    ergDictS1 = {}
    ergDictS2 = {}
    sumCounts = 0
    for i in s1:
        if i not in ergDictS1:
            ergDictS1[i] = 1
        else:
            ergDictS1[i] += 1
    for i in s2:
        if i not in ergDictS2:
            ergDictS2[i] = 1
        else:
            ergDictS2[i] += 1                
    print(ergDictS1)
    print(ergDictS2)
    
    workedList = []          
    for i in s1:
        if i in ergDictS1 and i in ergDictS2 and i not in workedList:
            if ergDictS1[i] >= ergDictS2[i]:
                sumCounts += ergDictS2[i]
            else:
                sumCounts += ergDictS1[i]
            workedList.append(i)
    return sumCounts   
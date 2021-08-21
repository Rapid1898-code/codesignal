<<<<<<< HEAD
def absoluteValuesSumMinimization(a):   
    minDiff = 999999999
    ergElem = False
    for e in a:
        tmpDiff = 0
        for f in a:
            tmpDiff += abs(f - e)
        if tmpDiff < minDiff:
            minDiff = tmpDiff
            ergElem = e
        elif tmpDiff == minDiff and e < ergElem:
            ergElem = e
    return (ergElem)   
=======
import itertools

def stringsRearrangement(inputArray):
    erg = itertools.permutations(inputArray)   
    
    for idx,combi in enumerate(erg):
        diffOneAll = True        
        for idx2,elem in enumerate(combi):            
            if idx2 == 0:
                continue
            tmpCountDiff = 0
            for i in range(len(elem)):
                if combi[idx2][i] != combi[idx2-1][i]:
                    tmpCountDiff += 1
            if tmpCountDiff != 1:
                diffOneAll = False
                break
        if diffOneAll == True:
            return True
    return False
            
>>>>>>> 4b94acf879545f0f689e02cff62fd0dee334746e

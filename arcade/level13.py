def reverseInParentheses(inputString):
    while "(" in inputString:
        print(f"String: {inputString}")    
        idx = startIDX = endIDX = 0        
        while True:
            if inputString[idx] == "(":
                startIDX = idx
            if inputString[idx] == ")":
                tmpString = inputString[startIDX+1:idx]
                tmpString = tmpString[::-1]
                inputString = inputString[:startIDX] + tmpString + inputString[idx+1:]
                break
            idx += 1
    return(inputString)
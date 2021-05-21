def arrayChange(inputArray):
    countMoves = 0
    for idx,elem in enumerate(inputArray):
        # print(f"DEBUG: CountMoves: {countMoves}")
        # print(f"DEBUG InputArray: {inputArray}")

        


        if idx == 0 or (inputArray[idx] > inputArray[idx-1]):
            continue
        countMoves += inputArray[idx -1] - inputArray[idx] + 1
        inputArray[idx] += inputArray[idx -1] - inputArray[idx] + 1
              
    return countMoves
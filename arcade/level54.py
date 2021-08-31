def sumUpNumbers(inputString):
    listString = list(inputString)
    newString = ""
    countSum = 0
    for char in listString:
        if char.isdigit():
            newString += char
        else:
            newString += " "

    newList = newString.split(" ")
    for elem in newList:
        if elem != "":
            countSum += int(elem)
    return countSum
def circleOfNumbers(n, firstNumber):
    middle = n // 2
    if firstNumber >= middle:
        return firstNumber - middle
    else:
        return firstNumber + middle
    
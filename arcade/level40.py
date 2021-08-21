def longestDigitsPrefix(inputString):
    prefix = ""
    for c in inputString:
        if c.isdigit():
            prefix += c
        else:
            break
    return prefix
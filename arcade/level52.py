def longestWord(text):
    longestWord = ""
    longestCount = 0
    text = text.replace(","," ").replace("!"," ").replace("?"," ").replace("["," ").replace("]"," ").replace("-"," ").replace("_"," ")
    for word in text.split(" "):
        count = 0
        for c in word:
            if c.isalpha():
                count += 1
       
        if count > longestCount:
            longestWord = word
            longestCount = count
    return longestWord
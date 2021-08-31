def messageFromBinaryCode(code):
    erg = ""
    for i,e in enumerate(code):
        if i % 8 == 0:
            dec = int(code[i:i+8],2)
            char = chr(dec)
            erg += char
            
            print(code[i:i+9], dec, char)
            
    return erg        
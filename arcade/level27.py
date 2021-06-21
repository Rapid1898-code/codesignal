def variableName(name):
    if name[0] in ["0","1","2","3","4","5","6","7","8","9"]:
        return False
    allowed = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","_"]        
    for c in name:
        if c.lower() not in allowed:
            return(False)
    return(True)
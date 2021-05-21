def centuryFromYear(year):
    if len(str(year)) == 4:
        if str(year)[2:] == "00":
            return int(str(year)[:2])        
        else:        
            return int(str(year)[:2]) + 1
    elif len(str(year)) == 3:
        if str(year)[1:] == "00":
            return int(str(year)[:1])        
        else:        
            return int(str(year)[:1]) + 1
    else:
        return 1
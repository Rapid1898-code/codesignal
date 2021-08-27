def validTime(time):
    hour = time.split(":")[0]
    minute = time.split(":")[1]
    if int(hour) > 23:
        return False
    if int(minute) > 59:
        return False
    return True
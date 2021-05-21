def addBorder(picture):
    for idx,elem in enumerate(picture):
        picture[idx] = "*" + elem + "*"
    strDefault = "*" * len(picture[idx])
    picture.insert(0,strDefault)
    picture.append(strDefault)
    return(picture)
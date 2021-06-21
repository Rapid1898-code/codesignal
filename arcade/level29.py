def chessBoardCellColor(cell1, cell2):
    if int(cell1[1]) % 2 == 1:
        if cell1[0] in ["A","C","E","G"]:
            cell1Color = "Black"
        else:
            cell1Color = "White"            
    else:
        if cell1[0] in ["B","D","F","H"]:
            cell1Color = "Black"
        else:
            cell1Color = "White"                        

    if int(cell2[1]) % 2 == 1:
        if cell2[0] in ["A","C","E","G"]:
            cell2Color = "Black"
        else:
            cell2Color = "White"            
    else:
        if cell2[0] in ["B","D","F","H"]:
            cell2Color = "Black"
        else:
            cell2Color = "White"                        
        
    if cell1Color == cell2Color:
        return True
    else:
        return False
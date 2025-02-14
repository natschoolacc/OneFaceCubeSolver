rows = []
corners = ["", "", "", ""]

def evaluateCorners():
    for x in corners:
        if x == "":
            corners[corners.index(x)] = evaluateCorners(corners.index(x))
    print(corners)

def evaluateCorner(corner):
    index = 0
    row = 0
    if corner == 1:
        index = 2
        row = 0
    elif corner == 2:
        index = 0
        row = 2
    elif corner == 3:
        index = 2
        row = 2
    return rows[row][index]

def rowInp(rowsT):
    rows = rowsT
    evaluateCorners()
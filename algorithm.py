import cornerData
rows = []
corners = ["0", "1", "2", "3"]
cornersFull = []
usedCorners = []
faces = []

def evaluateCorners():
    for x in corners:
        if x == "0" or x == "1" or x == "2" or x == "3":
            corners[corners.index(x)] = evaluateCorner(int(x))
            for y in cornerData.corners:
                if y.count(evaluateCorner(int(x))) >= 1 and usedCorners.count(cornerData.corners.index(y)) == 0:
                    cornersFull.insert(0, y)
                    usedCorners.insert(0, cornerData.corners.index(y))
                    break
    for y in cornerData.corners:
        if usedCorners.count(cornerData.corners.index(y)) == 1:
            cornersFull.append(y)
    print("The Corners of the cube you provided are:\n" + str(cornersFull))
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
    global rows
    rows = rowsT
    evaluateCorners()

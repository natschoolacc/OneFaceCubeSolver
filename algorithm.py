import cornerData
import sideData
rows = []
corners = ["0", "1", "2", "3"]
cornersFull = []
usedCorners = []
faces = []

def evaluateCorners():
    global cornersFull, usedCorners  # Declare global variables
    cornersFull = []  # Reset cornersFull to avoid stale data
    usedCorners = []  # Reset usedCorners to avoid stale data

    for x in corners:
        if x in ["0", "1", "2", "3"]:  # Check valid corner indices
            evaluated_corner = evaluateCorner(int(x))
            corners[corners.index(x)] = evaluated_corner
            for y in cornerData.corners:
                if evaluated_corner in y and cornerData.corners.index(y) not in usedCorners:
                    cornersFull.append(y)
                    usedCorners.append(cornerData.corners.index(y))
                    break
def mapCube():
    global cornersFull

    faces = {
        "front": {"center": "o", "corners": [], "edges": []},
        "back": {"center": "r", "corners": [], "edges": []},
        "left": {"center": "g", "corners": [], "edges": []},
        "right": {"center": "b", "corners": [], "edges": []},
        "top": {"center": "w", "corners": [], "edges": []},
        "bottom": {"center": "y", "corners": [], "edges": []},
    }

    # Map corners to faces properly
    for corner in cornersFull:
        # Front face corners (orange)
        if "o" in corner and corner not in faces["front"]["corners"]:
            faces["front"]["corners"].append(corner)
        
        # Back face corners (red)
        if "r" in corner and corner not in faces["back"]["corners"]:
            faces["back"]["corners"].append(corner)
            
        # Left face corners (green)
        if "g" in corner and corner not in faces["left"]["corners"]:
            faces["left"]["corners"].append(corner)
            
        # Right face corners (blue)
        if "b" in corner and corner not in faces["right"]["corners"]:
            faces["right"]["corners"].append(corner)
            
        # Top face corners (white)
        if "w" in corner and corner not in faces["top"]["corners"]:
            faces["top"]["corners"].append(corner)
            
        # Bottom face corners (yellow)
        if "y" in corner and corner not in faces["bottom"]["corners"]:
            faces["bottom"]["corners"].append(corner)

    # Rest of the code remains the same...

    # Map edges to faces
    for edge in sideData.side:
        if "o" in edge and edge not in faces["front"]["edges"]:
            faces["front"]["edges"].append(edge)
        if "r" in edge and edge not in faces["back"]["edges"]:
            faces["back"]["edges"].append(edge)
        if "g" in edge and edge not in faces["left"]["edges"]:
            faces["left"]["edges"].append(edge)
        if "b" in edge and edge not in faces["right"]["edges"]:
            faces["right"]["edges"].append(edge)
        if "w" in edge and edge not in faces["top"]["edges"]:
            faces["top"]["edges"].append(edge)
        if "y" in edge and edge not in faces["bottom"]["edges"]:
            faces["bottom"]["edges"].append(edge)

    # Print the mapped cube
    for face, data in faces.items():
        print(f"{face.capitalize()} Face:")
        print(f"  Center: {data['center']}")
        print(f"  Corners: {data['corners']}")
        print(f"  Edges: {data['edges']}")
        print()
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
    mapCube()

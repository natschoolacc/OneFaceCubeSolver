import algorithm

print("finds a possible solution to 5 sides of the rubix cube givin only one side:\n")
print("data should be givin left to right top to bottom")
print("exemple: w w w\n w w w\n w w w\n")
try:
    askForValues = False
    if askForValues:
        row1 = str(input("Row 1: ")).split(" ")
        row2 = str(input("Row 2: ")).split(" ")
        row3 = str(input("Row 3: ")).split(" ")
        rows = [row1, row2, row3]
    else:
        rows = [["r", "w", "g"], ["w", "w", "w"], ["b", "w", "y"]]



    algorithm.rowInp(rows)
except ValueError:
    print()
    #https://prod.liveshare.vsengsaas.visualstudio.com/join?07E6075E8F43DDE1CF05B5F495AC26E4CAC0
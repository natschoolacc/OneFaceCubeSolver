import algorithm

print("finds a possible solution to 5 sides of the rubix cube givin only one side:\n")
print("data should be givin left to right top to bottom")
print("exemple: w w w\n w w w\n w w w\n")
try:
    row1 = str(input("Row 1: "))
    row2 = str(input("Row 2: "))
    row3 = str(input("Row 3: "))
    rows = [row1, row2, row3]



    algorithm.rowInp(rows)
except ValueError:
    print()
    #https://prod.liveshare.vsengsaas.visualstudio.com/join?07E6075E8F43DDE1CF05B5F495AC26E4CAC0
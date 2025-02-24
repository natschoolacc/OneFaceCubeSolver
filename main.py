import algorithm

print("Finds possible solution to a standered rubix cube givin only one side:\n")
print("Data should be givin left to right top to bottom:")
print("Example: w w w\n         w w w\n         w w w\n")
try:
    askForValues = False
    if askForValues:
        row1 = str(input("Row 1: ")).split(" ")
        row2 = str(input("Row 2: ")).split(" ")
        row3 = str(input("Row 3: ")).split(" ")
        rows = [row1, row2, row3]
    else:
        rows = [["r", "w", "g"], 
               ["w", "w", "w"], 
               ["b", "w", "y"]]



    algorithm.rowInp(rows)
except ValueError:
    # Handle cases where invalid input is provided
    print("Error: Invalid input! Ensure that you provide three space-separated colors for each row.")
   
# How many safe tiles are there in a total of 400000 rows?

#-----------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day18-Like_a_Rogue\input.txt") as f:
    data = f.readlines()

#Given number of rows
numberOfRows = 400000

#List of rows with the given one put in
rows = [list(data[0].strip())]
#Lenght of the each row
rowLenght = len(rows[0])

#Until we find the desired number of rows
while len(rows) != numberOfRows:

    #List of tiles in the new row
    nextRow = []
    
    #For each tile in the new row
    for index in range(rowLenght):

        #If it is the left-most tile, left is safe
        if index == 0:
            l = "."
        #Check at upper left otherwise
        else:
            l = rows[-1][index-1]

        #If it is the right-most tile, right is safe
        if index == rowLenght-1:
            r = "."
        #Check upper right otherwise
        else:
            r = rows[-1][index+1]
        
        #Check upper center
        c = rows[-1][index]

        #Rule 1: tile is a trap if its left and center tiles are traps, but its right tile is not
        if l == c == "^" and r == ".":
            nextRow.append("^")
        #Rule 2: tile is a trap if its center and right tiles are traps, but its left tile is not
        elif l == "." and c == r == "^":
            nextRow.append("^")
        #Rule 3: tile is a trap if only its left tile is a trap
        elif l == "^" and c == r == ".":
            nextRow.append("^")
        #Rule 4: tile is a trap if only its right tile is a trap
        elif l == c == "." and r == "^":
            nextRow.append("^")
        #Safe tile otherwise
        else:
            nextRow.append(".")

    #Add the row to the list
    rows.append(nextRow)

#Safe tiles counter
safeTiles = 0

#For each row count its safe tiles
for row in rows:

    safeTiles += row.count(".")

print("There are {} safe tiles in the room".format(safeTiles))
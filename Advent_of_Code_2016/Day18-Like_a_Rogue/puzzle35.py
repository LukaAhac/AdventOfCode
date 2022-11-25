# As you enter this room, you hear a loud click! Some of the tiles in the floor here seem to be pressure 
# plates for traps, and the trap you just triggered has run out of... whatever it tried to do to you. 
# You doubt you'll be so lucky next time.

# Upon closer examination, the traps and safe tiles in this room seem to follow a pattern. 
# The tiles are arranged into rows that are all the same width; you take note of the safe 
# tiles (.) and traps (^) in the first row (your puzzle input).

# The type of tile (trapped or safe) in each row is based on the types of the tiles in the 
# same position, and to either side of that position, in the previous row. (If either side is 
# off either end of the row, it counts as "safe" because there isn't a trap embedded in the wall.)

# For example, suppose you know the first row (with tiles marked by letters) and want to 
# determine the next row (with tiles marked by numbers):

# ABCDE
# 12345
# The type of tile 2 is based on the types of tiles A, B, and C; the type of tile 5 is based on 
# tiles D, E, and an imaginary "safe" tile. Let's call these three tiles from the previous row the 
# left, center, and right tiles, respectively. Then, a new tile is a trap only in one of the 
# following situations:

# Its left and center tiles are traps, but its right tile is not.
# Its center and right tiles are traps, but its left tile is not.
# Only its left tile is a trap.
# Only its right tile is a trap.
# In any other situation, the new tile is safe.

# Then, starting with the row ..^^., you can determine the next row by applying those rules to each new tile:

# The leftmost character on the next row considers the left (nonexistent, so we assume "safe"), 
# center (the first ., which means "safe"), and right (the second ., also "safe") tiles on the previous row. 
# Because all of the trap rules require a trap in at least one of the previous three tiles, 
# the first tile on this new row is also safe, ..
# The second character on the next row considers its left (.), center (.), and right (^) tiles 
# from the previous row. This matches the fourth rule: only the right tile is a trap. Therefore, 
# the next tile in this new row is a trap, ^.
# The third character considers .^^, which matches the second trap rule: its center and right 
# tiles are traps, but its left tile is not. Therefore, this tile is also a trap, ^.
# The last two characters in this new row match the first and third rules, respectively, and so 
# they are both also traps, ^.
# After these steps, we now know the next row of tiles in the room: .^^^^. Then, we continue on to 
# the next row, using the same rules, and get ^^..^. After determining two new rows, our map looks like this:

# ..^^.
# .^^^^
# ^^..^
# Here's a larger example with ten tiles per row and ten rows:

# .^^.^.^^^^
# ^^^...^..^
# ^.^^.^.^^.
# ..^^...^^^
# .^^^^.^^.^
# ^^..^.^^..
# ^^^^..^^^.
# ^..^^^^.^^
# .^^^..^.^^
# ^^.^^^..^^
# In ten rows, this larger example has 38 safe tiles.

# Starting with the map in your puzzle input, in a total of 40 rows (including the starting row), 
# how many safe tiles are there?

#-----------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day18-Like_a_Rogue\input.txt") as f:
    data = f.readlines()

#Given number of rows
numberOfRows = 40

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
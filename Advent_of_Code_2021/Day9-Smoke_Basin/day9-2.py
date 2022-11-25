# Next, you need to find the largest basins so you know what areas are most important to avoid.

# A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, 
# although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations 
# will always be part of exactly one basin.

# The size of a basin is the number of locations within the basin, including the low point. The example above has 
# four basins.

# The top-left basin, size 3:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The top-right basin, size 9:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The middle basin, size 14:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The bottom-right basin, size 9:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

# What do you get if you multiply together the sizes of the three largest basins?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day9-Smoke_Basin\input.txt") as f:
    data = f.readlines()

#Given input
inp = []

#Parse input
for line in data:
    line = list(map(int,list(line.strip())))
    inp.append(line)


#Size of the floor
xMax = len(inp[0])
yMax = len(inp)
#Variable for summing lowpoints
lowPointsList = []

#For every location
for y in range(len(inp)):

    for x in range(len(inp[0])):

        #Adjecent locations
        neighbourLoc = []

        #If current location is not first row, add up
        if y > 0:
            neighbourLoc.append(inp[y-1][x])
        
        #If current location is not last row, add down
        if y< yMax-1:
            neighbourLoc.append(inp[y+1][x])

        #If current location is not first column, add left
        if x > 0:
            neighbourLoc.append(inp[y][x-1])

        #If current location is not last column, add right
        if x < xMax-1:
            neighbourLoc.append(inp[y][x+1])

        #Initially make a point as lowpoint
        lowPoint = True

        #If any of adjecent points are smaller or equal to the point then the point is not a lowpoint
        for height in neighbourLoc:

            if inp[y][x] >= height:
                lowPoint  = False

        #If the point is the lowpoint add its value + 1 to the sum
        if lowPoint:
            lowPointsList.append((y,x))

#List of basins
basins = []

#For each lowpoint
for point in lowPointsList:

    #Set of locations within that basin
    basinSet = set()
    #Add the lowpoint to the basin
    basinSet.add(point)
    #Get the current size of the basin
    size = len(basinSet)

    #Until we discovered whole basin
    while True:

        #Set where we add locations that we find
        newBasinSet = basinSet.copy()

        #For each location in the basin
        for location in basinSet:

            #Extract the coordinates
            y = location[0]
            x = location[1]
            
            #List of the adjecent locations to that locaiton
            neighbourLoc = []

            #If current location is not first row, add up
            if y > 0:
                neighbourLoc.append((y-1,x))

            #If current location is not last row, add down
            if y< yMax-1:
                neighbourLoc.append((y+1,x))

            #If current location is not first column, add left
            if x > 0:
                neighbourLoc.append((y,x-1))

            #If current location is not last column, add right
            if x < xMax-1:
                neighbourLoc.append((y,x+1))

            #For each adjecent location
            for location in neighbourLoc:

                #Get its height
                height = inp[location[0]][location[1]]

                #If the height is bigger than the height of the location that already is in the basin
                #and height is not 9, then expand the basin by adding new location
                if inp[y][x] < height and height != 9:
                    newBasinSet.add(location)
        
        #If the size of the basin at the end of the loop is the same as the size in the beginning of
        #then we didn't expand our basin because there is no more to expand to
        if size == len(newBasinSet):
            basins.append(basinSet)
            break
        #Else, we did expand, calculate new size and update the basin set
        else:
            size = len(newBasinSet)
            basinSet = newBasinSet

#List of the sizes of the basins
basinSizes = []

#For each basin
for basin in basins:

    #Append the size of the basin to the size list
    basinSizes.append(len(basin))

#Sort the basin sizes in descending order
basinSizes = sorted(basinSizes, reverse=True)

#Output
print("If you multiply together the sizes of the three largest basins you get :",basinSizes[0]*basinSizes[1]*basinSizes[2])
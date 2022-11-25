# You've finally met your match; the doors that provide access to the roof are locked tight, and all of the 
# controls and related electronics are inaccessible. You simply can't reach them.

# The robot that cleans the air ducts, however, can.

# It's not a very fast little robot, but you reconfigure it to be able to interface with some of the exposed 
# wires that have been routed through the HVAC system. If you can direct it to each of those locations, 
# you should be able to bypass the security controls.

# You extract the duct layout for this area from some blueprints you acquired and create a map with the relevant 
# locations marked (your puzzle input). 0 is your current location, from which the cleaning robot embarks; the 
# other numbers are (in no particular order) the locations the robot needs to visit at least once each. Walls are 
# marked as #, and open passages are marked as .. Numbers behave like open passages.

# For example, suppose you have a map like the following:

# ###########
# #0.1.....2#
# #.#######.#
# #4.......3#
# ###########
# To reach all of the points of interest as quickly as possible, you would have the robot take the following path:

# 0 to 4 (2 steps)
# 4 to 1 (4 steps; it can't move diagonally)
# 1 to 2 (6 steps)
# 2 to 3 (2 steps)
# Since the robot isn't very fast, you need to find it the shortest route. This path is the fewest steps (in the 
# above example, a total of 14) required to start at 0 and then visit every other location at least once.

# Given your actual map, and starting from location 0, what is the fewest number of steps required to visit 
# every non-0 number marked on the map at least once?

#-----------------------------------------------------------------------------------------------------------

from Lib import heapq

#Read input
with open(r"Day24-Air_Duct_Spelunking\input.txt") as f:
    data = f.readlines()

#Input
inp = []

numbers = set()

#Parse input
for line in data:
    line = list(line.strip())
    inp.append(line)

#Look for numbers that we have to visit, and retrive the starting coordinates
for xIndex in range(len(inp[0])):

    for yIndex in range(len(inp)):

        if inp[yIndex][xIndex] not in {"#","."}:

            numbers.add(inp[yIndex][xIndex])

            if inp[yIndex][xIndex] == "0":
                xStart = xIndex
                yStart = yIndex

#String that represents visited numbers, N - number at given index is not visited
#T - number at given index was visited, we set 0 to T, since we are at location 0 initially
init = "N" * len(numbers)
init = "T" + init[1:]

#Priority queue of states
states = []
heapq.heappush(states,[0,xStart,yStart,init])

#Cache for seen states, key is string representation of a steta(x-yVISITS), value is number of steps
#required to reach that state
seenStates = dict()
seenStates[str(xStart)+"-"+str(yStart)+init] = 0

#Until we find solution
while True:

    #Pop first
    curr = heapq.heappop(states)

    #If we visited all the numbers that is the solution
    if "TTTTTTTT" == curr[3]:

        print("The fewest number of steps required to visit every non-0 number marked on the map at least once is :",curr[0])
        exit()

    #Contrcut possible povements from the current location in every direction (Left,right,up,down)
    #Each elemtn will be next possible state given as (x,y,numberOfMoves)
    possibleLocations = []

    s = curr[0]
    currX = curr[1]
    currY = curr[2]

    while inp[currY-1][currX] != "#":

        s += 1
        possibleLocations.append([currX,currY-1,s])
        currY -= 1


    s = curr[0]
    currX = curr[1]
    currY = curr[2]

    while inp[currY+1][currX] != "#":

        s += 1
        possibleLocations.append([currX,currY+1,s])
        currY += 1

    s = curr[0]
    currX = curr[1]
    currY = curr[2]

    while inp[currY][currX-1] != "#":

        s += 1
        possibleLocations.append([currX-1,currY,s])
        currX -= 1

    s = curr[0]
    currX = curr[1]
    currY = curr[2]

    while inp[currY][currX+1] != "#":

        s += 1
        possibleLocations.append([currX+1,currY,s])
        currX += 1


    #For every possible location that we can move to
    for loc in possibleLocations:

        #Numbers visited
        newNums = curr[3]

        #If we end up on a location that is a number, mark it as visited
        if inp[loc[1]][loc[0]] not in {"#","."}:
            num = int(inp[loc[1]][loc[0]])
            newNums = list(curr[3])
            newNums[num] = "T"
            newNums = "".join(newNums)

        #Construct the string represtntation x-yVISITED
        stateString = str(loc[0]) + "-" + str(loc[1]) + newNums

        #If we have not already been in that state, add that state to the 
        #seen state list and to the priority queue
        if stateString not in seenStates:
            seenStates[stateString] = loc[2]
            heapq.heappush(states,[loc[2],loc[0],loc[1],newNums])
        #If we have been to that state but we have found a way with fewer steps
        #Replace the cost in seen state list and add that state to the priority queue
        elif seenStates[stateString] > loc[2]:
            seenStates[stateString] = loc[2]
            heapq.heappush(states,[loc[2],loc[0],loc[1],newNums])
    
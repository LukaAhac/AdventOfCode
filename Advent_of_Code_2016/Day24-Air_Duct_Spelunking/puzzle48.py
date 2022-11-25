# Of course, if you leave the cleaning robot somewhere weird, someone is bound to notice.

# What is the fewest number of steps required to start at 0, visit every non-0 number marked on 
# the map at least once, and then return to 0?

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
    if "TTTTTTTT" == curr[3] and curr[1] == xStart and curr[2] == yStart:

        print("The fewest number of steps required to start at 0, visit every non-0 number marked on the map at least once, and then return to 0 :",curr[0])
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
    
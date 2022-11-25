# You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can 
# barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it 
# would be best not to bump any of them.

# The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of 
# the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the 
# cave (your puzzle input). For example:

# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581
# You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. 
# The number at each position is its risk level; to determine the total risk of an entire path, add up the risk 
# levels of each position you enter (that is, don't count the risk level of your starting position unless you 
# enter it; leaving it adds no risk to your total).

# Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total 
# risk is highlighted here:

# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581
# The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).

# What is the lowest total risk of any path from the top left to the bottom right?

#----------------------------------------------------------------------------------------------------------------------

import heapq

#Read input
with open(r"Day15-Chiton\input.txt") as f:
    data = f.readlines()

#Given input
inp = []

#Parse input
for line in data:
    line = list(map(int,list(line.strip())))
    inp.append(line)

#Max coords
xMax = len(inp[0])
yMax = len(inp)

#Grid for storing the lowest risk value to get to grid location
locationSolved = [[None for _ in range(xMax)] for _ in range(yMax)]

#Priority queue (risk,x,y)
priorQueue = [(0,0,0)]

#Move directions
moveX = [0,1,0,-1]
moveY = [1,0,-1,0]

#Move in priority queue until solution is found
while priorQueue:

    #Pop the value from priotiy queue
    riskCost,x,y = heapq.heappop(priorQueue)
    #Check if we are within the grid
    if x<0 or x>xMax-1 or y<0 or y>yMax-1:
        continue

    #If we havent solved that location, or we found better solution, mark it
    if locationSolved[y][x] is None or riskCost + inp[y][x] < locationSolved[y][x]:
        locationSolved[y][x] = riskCost + inp[y][x]
    #If we found worse soltuion go next
    else:
        continue

    #If we reached bottom right corner thats it
    if x == xMax-1 and y == yMax-1:
        break

    #Move to each direction
    for d in range(4):
        dy = y + moveX[d]
        dx = x + moveY[d]

        heapq.heappush(priorQueue,(locationSolved[y][x],dx,dy))

print("The lowest total risk of any path from the top left to the bottom right is :",locationSolved[yMax-1][xMax-1]-inp[0][0])
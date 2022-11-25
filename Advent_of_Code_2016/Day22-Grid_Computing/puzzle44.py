# Now that you have a better understanding of the grid, it's time to get to work.

# Your goal is to gain access to the data which begins in the node with y=0 and the highest x 
# (that is, the node in the top-right corner).

# For example, suppose you have the following grid:

# Filesystem            Size  Used  Avail  Use%
# /dev/grid/node-x0-y0   10T    8T     2T   80%
# /dev/grid/node-x0-y1   11T    6T     5T   54%
# /dev/grid/node-x0-y2   32T   28T     4T   87%
# /dev/grid/node-x1-y0    9T    7T     2T   77%
# /dev/grid/node-x1-y1    8T    0T     8T    0%
# /dev/grid/node-x1-y2   11T    7T     4T   63%
# /dev/grid/node-x2-y0   10T    6T     4T   60%
# /dev/grid/node-x2-y1    9T    8T     1T   88%
# /dev/grid/node-x2-y2    9T    6T     3T   66%
# In this example, you have a storage grid 3 nodes wide and 3 nodes tall. The node you can access directly, 
# node-x0-y0, is almost full. The node containing the data you want to access, node-x2-y0 (because it has y=0 and 
# the highest x value), contains 6 terabytes of data - enough to fit on your node, if only you could make enough 
# space to move it there.

# Fortunately, node-x1-y1 looks like it has enough free space to enable you to move some of this data around. 
# In fact, it seems like all of the nodes have enough space to hold any node's data (except node-x0-y2, which is 
# much larger, very full, and not moving any time soon). So, initially, the grid's capacities and connections look 
# like this:

# ( 8T/10T) --  7T/ 9T -- [ 6T/10T]
#     |           |           |
#   6T/11T  --  0T/ 8T --   8T/ 9T
#     |           |           |
#  28T/32T  --  7T/11T --   6T/ 9T
# The node you can access directly is in parentheses; the data you want starts in the node marked by square brackets.

# In this example, most of the nodes are interchangable: they're full enough that no other node's data would fit, 
# but small enough that their data could be moved around. Let's draw these nodes as .. The exceptions are the empty node, 
# which we'll draw as _, and the very large, very full node, which we'll draw as #. Let's also draw the goal 
# data as G. Then, it looks like this:

# (.) .  G
#  .  _  .
#  #  .  .
# The goal is to move the data in the top right, G, to the node in parentheses. To do this, we can issue some commands 
# to the grid and rearrange the data:

# Move data from node-y0-x1 to node-y1-x1, leaving node node-y0-x1 empty:

# (.) _  G
#  .  .  .
#  #  .  .
# Move the goal data from node-y0-x2 to node-y0-x1:

# (.) G  _
#  .  .  .
#  #  .  .
# At this point, we're quite close. However, we have no deletion command, so we have to move some more data around. 
# So, next, we move the data from node-y1-x2 to node-y0-x2:

# (.) G  .
#  .  .  _
#  #  .  .
# Move the data from node-y1-x1 to node-y1-x2:

# (.) G  .
#  .  _  .
#  #  .  .
# Move the data from node-y1-x0 to node-y1-x1:

# (.) G  .
#  _  .  .
#  #  .  .
# Next, we can free up space on our node by moving the data from node-y0-x0 to node-y1-x0:

# (_) G  .
#  .  .  .
#  #  .  .
# Finally, we can access the goal data by moving the it from node-y0-x1 to node-y0-x0:

# (G) _  .
#  .  .  .
#  #  .  .
# So, after 7 steps, we've accessed the data we want. Unfortunately, each of these moves takes time, and we need to 
# be efficient:

# What is the fewest number of steps required to move your goal data to node-x0-y0?

#-----------------------------------------------------------------------------------------------------------

import copy

#Read input
with open(r"Day22-Grid_Computing\input.txt") as f:
    data = f.readlines()

#List of nodes
nodes = []

#Append nodes to the list
for line in data:
    nodes.append(line.strip().split())

#Remove the header
nodes = nodes[2:]
nodesDict = dict()

#This will be min and max values of the coordinates
xMin = 0
yMin = 0
xMax = 0
yMax = 0
#This will be the coordinate of the empty disk
x_empty = None
y_empty = None

#Transfrom nodes to dictionaries with integer data
for index in range(len(nodes)):
    name,x,y = nodes[index][0].split("-")

    #If its the empty node, get his coordinates
    if int(nodes[index][2][:-1]) == 0:
        x_empty = int(x[1:])
        y_empty = int(y[1:])

    if int(x[1:]) > xMax:
        xMax = int(x[1:])
    if int(y[1:]) > yMax:
        yMax = int(y[1:])

    nodesDict[int(x[1:]),int(y[1:])] = [int(nodes[index][1][:-1]),int(nodes[index][2][:-1]),int(nodes[index][3][:-1])]


#Class to represent each state while we take steps
class State():

    #Constructor
    def __init__(self,nodes,data_x,data_y,empty_x,empty_y,steps):
        self.nodes = nodes
        self.dataOn = [data_x,data_y]
        self.emptyOn = [empty_x,empty_y]
        self.steps = steps

    #Function that computes nexxt possible moves(states) from the given state
    def nextStates(self):

        global xMin
        global xMax
        global yMin
        global yMax
        
        #List for new states
        newStates = []

        #List of coordinates from which we move data to current coordinate
        candidateCoordinates = []
        #Coordiantes of the empty node
        x = self.emptyOn[0]
        y = self.emptyOn[1]
            
        #Check which coordintaes we can go to -> checks for edges and  corners
        if x > xMin:
            candidateCoordinates.append((x-1,y))
        if x < xMax:
             candidateCoordinates.append((x+1,y))
        if y > yMin:
             candidateCoordinates.append((x,y-1))
        if y < yMax:
            candidateCoordinates.append((x,y+1))

        #For each coordiante
        for coordinate in candidateCoordinates:
            
            #If the data from the node on the given coordiante cannot fit on the empty disk, continue
            if self.nodes[(x,y)][2] < self.nodes[coordinate][1]:
                continue

            #Else, create a new state
            #Copy the nodes
            newNodes = copy.deepcopy(self.nodes)
            #Update usage and avialibility on the emptydisk
            newNodes[(x,y)][2] -= self.nodes[coordinate][1]
            newNodes[(x,y)][1] += self.nodes[coordinate][1]
            #Update usage and avialibility on the disk we transfer data from
            newNodes[coordinate][1] = 0
            newNodes[coordinate][2] = newNodes[coordinate][0]

            #If we moved the node that has data we want, then give the new states the coordinate where the data is
            if coordinate[0] == self.dataOn[0] and coordinate[1] == self.dataOn[1]:
                newStates.append(State(newNodes,x,y,coordinate[0],coordinate[1],self.steps+1))
            #If we did not move the desired data, then just create a new state
            else:
                newStates.append(State(newNodes,self.dataOn[0],self.dataOn[1],coordinate[0],coordinate[1],self.steps+1))

        #Return list of states that we can go to
        return newStates

    #Function that returns the string representation of the state
    #We only track where the data is and where the empty disk is
    def toString(self):

        global xMax
        global yMax

        stateAsString = str(self.emptyOn[0]) + "-" + str(self.emptyOn[1]) + "|"
        stateAsString += str(self.dataOn[0]) + "-" + str(self.dataOn[1])

        return stateAsString

    #Function that checks if the state is a goal state
    def solutionFound(self):

        if self.dataOn[0] == 0 and self.dataOn[1] == 0:
            return True

        return False


#We begin from with given nodes state, data is on (xMax,0), we found empty node to be on (x_empty,y_empty)
#and we set steps to 0 initially
currentStates = [State(nodesDict,xMax,0,x_empty,y_empty,0)]
#Add the initial state to the seenStates
seenStates = {currentStates[0].toString()}

#Grid that tracks the fastest state to get desired data from (xMax,0) to the grid location
#We index grid with (y,x) because the first index corresponds to the rows and second to the columns
gridFastest = [[None]*(xMax+1)]*(yMax+1)
#Add the begging state to the grid (xMax,0)
gridFastest[0][xMax] = currentStates[0]
#List of states that are fastest states to deliver data to some location in the grid
foundStates = [currentStates[0]]

#Until we find solution
while True:

    #List for next states
    nextStates = []
    #Flag that indicates where or not we found some states that are fastest to deliver the data to some point
    #in this iteration of the loop
    found = False

    #For each current state
    for state in currentStates:

        #Retrive the current data location
        dataX = state.dataOn[0]
        dataY = state.dataOn[1]

        #If we dont have the fastest state for that location, or this is even faster state
        if gridFastest[dataY][dataX] is None or gridFastest[dataY][dataX].steps > state.steps:

            #Add it to the grid
            gridFastest[dataY][dataX] = state
            #Add it to the list
            foundStates.append(state)
            #Set the flag
            found = True

        #Check if that state is the solution
        if state.solutionFound():
            print("The fewest number of steps required to move your goal data to node-x0-y0 is :",state.steps)
            quit()

        #Determine the next states if it is not solution
        nextStates += state.nextStates()

    #If we found some new state with fastest data delivery to some grid location
    #NOTE: With this way we are slowly finding the best ways the move the data to each location
    #around the initial location until we reach the desired location which is (0,0)
    if found:
        #The reset the current states to list of the fastest states
        currentStates = foundStates
        #Loop again
        continue
        

    #Else, erease all current states
    currentStates = []

    #For each new states check if we already seen that state
    for state in nextStates:

        stateString = state.toString()

        if stateString not in seenStates:
            #If we did not see the state, mark it as seen and add it to the current state list
            seenStates.add(stateString)
            currentStates.append(state)
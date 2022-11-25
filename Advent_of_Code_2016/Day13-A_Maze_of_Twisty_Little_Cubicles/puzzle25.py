# You arrive at the first floor of this new building to discover a much less welcoming environment than 
# the shiny atrium of the last one. Instead, you are in a maze of twisty little cubicles, all alike.

# Every location in this area is addressed by a pair of non-negative integers (x,y). Each such coordinate 
# is either a wall or an open space. You can't move diagonally. The cube maze starts at 0,0 and seems to 
# extend infinitely toward positive x and y; negative values are invalid, as they represent a location outside 
# the building. You are in a small waiting area at 1,1.

# While it seems chaotic, a nearby morale-boosting poster explains, the layout is actually quite logical. 
# You can determine whether a given x,y coordinate will be a wall or an open space using a simple system:

# Find x*x + 3*x + 2*x*y + y + y*y.
# Add the office designer's favorite number (your puzzle input).
# Find the binary representation of that sum; count the number of bits that are 1.
# If the number of bits that are 1 is even, it's an open space.
# If the number of bits that are 1 is odd, it's a wall.
# For example, if the office designer's favorite number were 10, drawing walls as # and open spaces as ., 
# the corner of the building containing 0,0 would look like this:

#   0123456789
# 0 .#.####.##
# 1 ..#..#...#
# 2 #....##...
# 3 ###.#.###.
# 4 .##..#..#.
# 5 ..##....#.
# 6 #...##.###
# Now, suppose you wanted to reach 7,4. The shortest route you could take is marked as O:

#   0123456789
# 0 .#.####.##
# 1 .O#..#...#
# 2 #OOO.##...
# 3 ###O#.###.
# 4 .##OO#OO#.
# 5 ..##OOO.#.
# 6 #...##.###
# Thus, reaching 7,4 would take a minimum of 11 steps (starting from your current location, 1,1).

# What is the fewest number of steps required for you to reach 31,39?

# Your puzzle input is 1362.

#-----------------------------------------------------------------------------------------------------------

#Input data given in task
data = 1362
xGoal = 31
yGoal = 39
xStart = 1
yStart = 1

#Class to represent each state while we take steps
class State():

    #Constructor
    def __init__(self,x,y,stepsTaken):
        self.x = x
        self.y = y
        self.stepsTaken = stepsTaken

    #Function that computes nexxt possible moves(states) from the given state
    def nextStates(self):

        #Thats favourite number
        global data

        #List for possible candidates
        candidateStates = []

        #Add all the possible moves - left,right,up,down
        if self.x != 0:
            candidateStates.append((self.x-1,self.y))
        candidateStates.append((self.x+1,self.y))
        if self.y != 0:
            candidateStates.append((self.x, self.y-1))
        candidateStates.append((self.x, self.y+1))

        #New states that are not walls
        newStates = []
        #Check if the (x,y) is wall, add it to the list if it is not
        for state in candidateStates:

            if self.wallOrSpace(state[0],state[1],data) == "space":
                newStates.append(State(state[0],state[1],self.stepsTaken+1))

        return newStates

    #Function that returns whether the current coordinate is wall or space
    def wallOrSpace(self,x,y,favouriteNum):

        #Given formula
        result = x*x + 3*x + 2*x*y + y +y*y + favouriteNum
        #Integer to bits
        binaryRepresentation = "{0:b}".format(result)
        #Count ones
        numberOfOnes = binaryRepresentation.count("1")
        #Decide the parity
        if numberOfOnes % 2 == 0:
            return "space"
        else:
            return "wall"

    #Function that returns the string representation of the state
    def toString(self):

        return str(self.x)+"-"+str(self.y)

    #Function that checks if the state is a goal state
    def solutionFound(self):

        global xGoal,yGoal

        if self.x == xGoal and self.y == yGoal:
            return True

        return False



#We begin from (1,1)
currentStates = [State(xStart,yStart,0)]
seenStates = [currentStates[0].toString()]

#Until we find solution
while True:

    #List for next states
    nextStates = []

    #For each current state
    for state in currentStates:

        #Check if it is solution
        if state.solutionFound():
            print("The fewest number of steps required for you to reach 31,39 is:",state.stepsTaken)
            quit()

        #Determine the next states if it is not solution
        nextStates += state.nextStates()

    #Erase current states
    currentStates = []

    #For each new states check if we already seen that state
    for state in nextStates:

        stateString = state.toString()

        if stateString not in seenStates:
            #If we did not see the state, mark it as seen and add it to the current state list
            seenStates.append(stateString)
            currentStates.append(state)
# How many locations (distinct x,y coordinates, including your starting location) can you reach 
# in at most 50 steps?

#-----------------------------------------------------------------------------------------------------------

#Input data given in task
data = 1362
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

#We begin from (1,1)
currentStates = [State(xStart,yStart,0)]
seenStates = [currentStates[0].toString()]

#Until we reach 50 steps
while True:

    #List for next states
    nextStates = []

    #For each current state
    for state in currentStates:

        #Determine the next states
        nextStates += state.nextStates()

    #Erase current states
    currentStates = []

    #For each new states check if we took more than 50 steps and if we already seen that state
    for state in nextStates:

        if state.stepsTaken >50:
            continue

        stateString = state.toString()

        if stateString not in seenStates:
            #If we did not see the state, mark it as seen and add it to the current state list
            seenStates.append(stateString)
            currentStates.append(state)

    #If there are no more states to work on, break the loop
    if len(currentStates) == 0:
        break


print("You can reach {} locations in at most 50 steps".format(len(seenStates)))
# You step into the cleanroom separating the lobby from the isolated area and put on the hazmat suit.

# Upon entering the isolated containment area, however, you notice some extra parts on the first floor
#  that weren't listed on the record outside:

# An elerium generator.
# An elerium-compatible microchip.
# A dilithium generator.
# A dilithium-compatible microchip.
# These work just like the other generators and microchips. You'll have to get them up to assembly as well.

# What is the minimum number of steps required to bring all of the objects, including these four new ones, 
# to the fourth floor?


#-----------------------------------------------------------------------------------------------------------
import itertools

#Given input
floors = [{"E","TG","TM","PlG","SG","EG","EM","DG","DM"},{"PlM","SM"},{"PrG","PrM","RG","RM"},set()]

class State():

    #Constructor
    def __init__(self, floors, elevatorAtFloor, numberOfSteps):
        self.floors = floors
        self.elevatorAtFloor = elevatorAtFloor
        self.numberOfSteps = numberOfSteps
        self.newStates = []

    #Function to check if the current state is the solution
    def solutionFound(self):

        #If all the objects are on the last floor we found the solution (10 objects + elevator)
        if len(self.floors[3]) == 15:
            return True
        return False

    #Function to check wheter or not the given floor is valid
    def checkIfFloorIsValid(self,floorState):
        
        #Generators and microchips on that floor
        generators = set()
        microchips = set()

        #Distinct generatros from microchips
        for object in floorState:
            if object[-1] == "G":
                generators.add(object[:-1])
            else:
                microchips.add(object[:-1])


        #If there are no generators or the microchips on the floor we are fine
        if len(generators) == 0 or len(microchips) == 0:
            return True

        #If there are both of them check if each microchip have its correspoding generator
        for microchip in microchips:
            #If it does not have it, return False
            if microchip not in generators:
                return False
        #True otherwise
        return True

    #Function to generate new states from the current states
    def nextStates(self):

        #List of possible states
        possibleStates = []

        #Get the objects on the current floor
        objects = self.floors[self.elevatorAtFloor]
        #Remove elevator form the objects
        objects.remove("E")

        #Make states where we take only one object from the floor
        for element in objects:
            possibleStates.append({element})
        #Add states where we take any two objects from the floor
        possibleStates += list(itertools.combinations(objects,2))
        
        #For each possible state check if it would leave us with valid floor states
        for possibleState in possibleStates:

            #Construct the new floor states
            nextCurrentFloorState = self.floors[self.elevatorAtFloor].copy()
            if self.elevatorAtFloor != 3:
                nextUpperFloorState = self.floors[self.elevatorAtFloor+1].copy()
            if self.elevatorAtFloor != 0:
                nextLowerFloorState = self.floors[self.elevatorAtFloor-1].copy()

            for element in possibleState:
                nextCurrentFloorState.remove(element)
                if self.elevatorAtFloor != 3:
                    nextUpperFloorState.add(element)
                if self.elevatorAtFloor != 0:
                    nextLowerFloorState.add(element)

            #If the current floor would be left not valid, continue
            if not self.checkIfFloorIsValid(nextCurrentFloorState):
                continue
            
            #Check if we can go one floor up
            if self.elevatorAtFloor != 3:
                if self.checkIfFloorIsValid(nextUpperFloorState):
                    nextFloors = self.floors.copy()
                    nextFloors[self.elevatorAtFloor] = nextCurrentFloorState.copy()
                    nextFloors[self.elevatorAtFloor+1] = nextUpperFloorState.copy()
                    nextFloors[self.elevatorAtFloor+1].add("E")
                    self.newStates.append(State(nextFloors,self.elevatorAtFloor+1,self.numberOfSteps+1))
            #Check if we can go one floor down
            if self.elevatorAtFloor != 0:
                if self.checkIfFloorIsValid(nextLowerFloorState):
                    nextFloors = self.floors.copy()
                    nextFloors[self.elevatorAtFloor] = nextCurrentFloorState.copy()
                    nextFloors[self.elevatorAtFloor-1] = nextLowerFloorState.copy()
                    nextFloors[self.elevatorAtFloor-1].add("E")
                    self.newStates.append(State(nextFloors,self.elevatorAtFloor-1,self.numberOfSteps+1))

        return self.newStates

    #Function that returns the string representation of the given state
    def stringRepresentation(self):

        stateString = ""

        for element in self.floors:

           stateString +=  "".join(sorted(element))
           stateString += "-"

        return stateString

#Initial state
allStates = [State(floors,0,0)]
#String representation of the first state
seenStates = {allStates[0].stringRepresentation()}

#Until we find the solution
while True:

    #List for candidate states
    possibleStates = []

    #Track progress
    #print(len(allStates),len(seenStates))

    #For each state
    for state in allStates:

        #Look if it is a solution
        if state.solutionFound():
            print("The minimum number of steps required to bring all of the objects to the fourth floor is:",state.numberOfSteps)
            exit()

        #If it is not calculate all possible states from that given state
        possibleStates += state.nextStates()

    #Erase last states
    allStates = []

    #For every new state
    for state in possibleStates:

        #Get the string representation of the state
        stateString = state.stringRepresentation()

        #If we did not already see this state, add it to the new states, and seen states
        if stateString not in seenStates:
            seenStates.add(stateString)
            allStates.append(state)
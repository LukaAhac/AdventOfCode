# You come upon a column of four floors that have been entirely sealed off from the rest of the building 
# except for a small dedicated lobby. There are some radiation warnings and a big sign which reads 
# "Radioisotope Testing Facility".

# According to the project status board, this facility is currently being used to experiment with 
# Radioisotope Thermoelectric Generators (RTGs, or simply "generators") that are designed to be paired
#  with specially-constructed microchips. Basically, an RTG is a highly radioactive rock that generates 
#  electricity through heat.

# The experimental RTGs have poor radiation containment, so they're dangerously radioactive. The chips are 
# prototypes and don't have normal radiation shielding, but they do have the ability to generate an 
# electromagnetic radiation shield when powered. Unfortunately, they can only be powered by their 
# corresponding RTG. An RTG powering a microchip is still dangerous to other microchips.

# In other words, if a chip is ever left in the same area as another RTG, and it's not connected to its 
# own RTG, the chip will be fried. Therefore, it is assumed that you will follow procedure and keep chips 
# connected to their corresponding RTG when they're in the same room, and away from other RTGs otherwise.

# These microchips sound very interesting and useful to your current activities, and you'd like to try to 
# retrieve them. The fourth floor of the facility has an assembling machine which can make a self-contained, 
# shielded computer for you to take with you - that is, if you can bring it all of the RTGs and microchips.

# Within the radiation-shielded part of the facility (in which it's safe to have these pre-assembly RTGs), 
# there is an elevator that can move between the four floors. Its capacity rating means it can carry at most 
# yourself and two RTGs or microchips in any combination. (They're rigged to some heavy diagnostic 
# equipment - the assembling machine will detach it for you.) As a security measure, the elevator will only 
# function if it contains at least one RTG or microchip. The elevator always stops on each floor to recharge, 
# and this takes long enough that the items within it and the items on that floor can irradiate each other. 
# (You can prevent this if a Microchip and its Generator end up on the same floor in this way, 
# as they can be connected while the elevator is recharging.)

# You make some notes of the locations of each component of interest (your puzzle input). 
# Before you don a hazmat suit and start moving things around, you'd like to have an idea of what you need to do.

# When you enter the containment area, you and the elevator will start on the first floor.

# For example, suppose the isolated area has the following arrangement:

# The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# The second floor contains a hydrogen generator.
# The third floor contains a lithium generator.
# The fourth floor contains nothing relevant.
# As a diagram (F# for a Floor number, E for Elevator, H for Hydrogen, L for Lithium, M for Microchip, 
# and G for Generator), the initial state looks like this:

# F4 .  .  .  .  .  
# F3 .  .  .  LG .  
# F2 .  HG .  .  .  
# F1 E  .  HM .  LM 
# Then, to get everything up to the assembling machine on the fourth floor, the following steps could be taken:

# Bring the Hydrogen-compatible Microchip to the second floor, which is safe because it can get power from the 
# Hydrogen Generator:

# F4 .  .  .  .  .  
# F3 .  .  .  LG .  
# F2 E  HG HM .  .  
# F1 .  .  .  .  LM 
# Bring both Hydrogen-related items to the third floor, which is safe because the Hydrogen-compatible microchip 
# is getting power from its generator:

# F4 .  .  .  .  .  
# F3 E  HG HM LG .  
# F2 .  .  .  .  .  
# F1 .  .  .  .  LM 
# Leave the Hydrogen Generator on floor three, but bring the Hydrogen-compatible Microchip back down with you 
# so you can still use the elevator:

# F4 .  .  .  .  .  
# F3 .  HG .  LG .  
# F2 E  .  HM .  .  
# F1 .  .  .  .  LM 
# At the first floor, grab the Lithium-compatible Microchip, which is safe because Microchips don't affect 
# each other:

# F4 .  .  .  .  .  
# F3 .  HG .  LG .  
# F2 .  .  .  .  .  
# F1 E  .  HM .  LM 
# Bring both Microchips up one floor, where there is nothing to fry them:

# F4 .  .  .  .  .  
# F3 .  HG .  LG .  
# F2 E  .  HM .  LM 
# F1 .  .  .  .  .  
# Bring both Microchips up again to floor three, where they can be temporarily connected to their corresponding 
# generators while the elevator recharges, preventing either of them from being fried:

# F4 .  .  .  .  .  
# F3 E  HG HM LG LM 
# F2 .  .  .  .  .  
# F1 .  .  .  .  .  
# Bring both Microchips to the fourth floor:

# F4 E  .  HM .  LM 
# F3 .  HG .  LG .  
# F2 .  .  .  .  .  
# F1 .  .  .  .  .  
# Leave the Lithium-compatible microchip on the fourth floor, but bring the Hydrogen-compatible one so you can 
# still use the elevator; this is safe because although the Lithium Generator is on the destination floor, 
# you can connect Hydrogen-compatible microchip to the Hydrogen Generator there:

# F4 .  .  .  .  LM 
# F3 E  HG HM LG .  
# F2 .  .  .  .  .  
# F1 .  .  .  .  .  
# Bring both Generators up to the fourth floor, which is safe because you can connect the Lithium-compatible 
# Microchip to the Lithium Generator upon arrival:

# F4 E  HG .  LG LM 
# F3 .  .  HM .  .  
# F2 .  .  .  .  .  
# F1 .  .  .  .  .  
# Bring the Lithium Microchip with you to the third floor so you can use the elevator:

# F4 .  HG .  LG .  
# F3 E  .  HM .  LM 
# F2 .  .  .  .  .  
# F1 .  .  .  .  .  
# Bring both Microchips to the fourth floor:

# F4 E  HG HM LG LM 
# F3 .  .  .  .  .  
# F2 .  .  .  .  .  
# F1 .  .  .  .  .  
# In this arrangement, it takes 11 steps to collect all of the objects at the fourth floor for assembly. 
# (Each elevator stop counts as one step, even if nothing is added to or removed from it.)

# In your situation, what is the minimum number of steps required to bring all of the objects to the fourth floor?

#-----------------------------------------------------------------------------------------------------------
import itertools

#Given input
floors = [{"E","TG","TM","PlG","SG"},{"PlM","SM"},{"PrG","PrM","RG","RM"},set()]

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
        if len(self.floors[3]) == 11:
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
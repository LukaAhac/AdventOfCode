# A group of amphipods notice your fancy submarine and flag you down. "With such an impressive shell," one amphipod says, 
# "surely you can help us with a question that has stumped our best scientists."

# They go on to explain that a group of timid, stubborn amphipods live in a nearby burrow. Four types of amphipods live 
# there: Amber (A), Bronze (B), Copper (C), and Desert (D). They live in a burrow that consists of a hallway and 
# four side rooms. The side rooms are initially full of amphipods, and the hallway is initially empty.

# They give you a diagram of the situation (your puzzle input), including locations of each amphipod (A, B, C, or D, 
# each of which is occupying an otherwise open space), walls (#), and open space (.).

# For example:

# #############
# #...........#
# ###B#C#B#D###
#   #A#D#C#A#
#   #########
# The amphipods would like a method to organize every amphipod into side rooms so that each side room contains one type 
# of amphipod and the types are sorted A-D going left to right, like this:

# #############
# #...........#
# ###A#B#C#D###
#   #A#B#C#D#
#   #########
# Amphipods can move up, down, left, or right so long as they are moving into an unoccupied open space. Each type of 
# amphipod requires a different amount of energy to move one step: Amber amphipods require 1 energy per step, Bronze 
# amphipods require 10 energy, Copper amphipods require 100, and Desert ones require 1000. The amphipods would like you 
# to find a way to organize the amphipods that requires the least total energy.

# However, because they are timid and stubborn, the amphipods have some extra rules:

# Amphipods will never stop on the space immediately outside any room. They can move into that space so long as they 
# immediately continue moving. (Specifically, this refers to the four open spaces in the hallway that are directly above 
# an amphipod starting position.)
# Amphipods will never move from the hallway into a room unless that room is their destination room and that room 
# contains no amphipods which do not also have that room as their own destination. If an amphipod's starting room is 
# not its destination room, it can stay in that room until it leaves the room. (For example, an Amber amphipod will not 
# move from the hallway into the right three rooms, and will only move into the leftmost room if that room is empty or 
# if it only contains other Amber amphipods.)
# Once an amphipod stops moving in the hallway, it will stay in that spot until it can move into a room. (That is, 
# once any amphipod starts moving, any other amphipods currently in the hallway are locked in place and will not move 
# again until they can move fully into a room.)
# In the above example, the amphipods can be organized using a minimum of 12521 energy. One way to do this is shown below.

# Starting configuration:

# #############
# #...........#
# ###B#C#B#D###
#   #A#D#C#A#
#   #########
# One Bronze amphipod moves into the hallway, taking 4 steps and using 40 energy:

# #############
# #...B.......#
# ###B#C#.#D###
#   #A#D#C#A#
#   #########
# The only Copper amphipod not in its side room moves there, taking 4 steps and using 400 energy:

# #############
# #...B.......#
# ###B#.#C#D###
#   #A#D#C#A#
#   #########
# A Desert amphipod moves out of the way, taking 3 steps and using 3000 energy, and then the Bronze amphipod 
# takes its place, taking 3 steps and using 30 energy:

# #############
# #.....D.....#
# ###B#.#C#D###
#   #A#B#C#A#
#   #########
# The leftmost Bronze amphipod moves to its room using 40 energy:

# #############
# #.....D.....#
# ###.#B#C#D###
#   #A#B#C#A#
#   #########
# Both amphipods in the rightmost room move into the hallway, using 2003 energy in total:

# #############
# #.....D.D.A.#
# ###.#B#C#.###
#   #A#B#C#.#
#   #########
# Both Desert amphipods move into the rightmost room using 7000 energy:

# #############
# #.........A.#
# ###.#B#C#D###
#   #A#B#C#D#
#   #########
# Finally, the last Amber amphipod moves into its room, using 8 energy:

# #############
# #...........#
# ###A#B#C#D###
#   #A#B#C#D#
#   #########
# What is the least energy required to organize the amphipods?

#----------------------------------------------------------------------------------------------------------------------
from Lib import heapq

#Read input
with open(r"Day23-Amphipod\input.txt") as f:
    data = f.readlines()
    
#Given input
inp = []

#Parse input
for line in data:
    line = line.strip()
    inp.append(line)

#Set up the starting state where room1 is first rome to the left and room4 is last room to the right
room1 = inp[2][3] + inp[3][1]
room2 = inp[2][5] + inp[3][3]
room3 = inp[2][7] + inp[3][5]
room4 = inp[2][9] + inp[3][7]
#Construct empty hallway
hallway = ["." for _ in range(len(inp[1])-2)]
hallwayLen = len(hallway)

#Making a list class only to override __lt__ 
#Doing that because heapq uses that function to determin which object is smaller and whic is bigger
#And by default when comparing lists __lt__ compares the first element of the lists and if they are the same
#it continues to the next one etc..
#Making this because i already wrote the code down there where the COST is the last element of the list
#And it was easier to do this than to put the cost onto the first place in the list
class MyList(list):

    def __lt__(self, other):
        return self[-1] < other[-1]

#Energy needed to move each type of amphipods - given in task
costToMove = {"A":1,"B":10,"C":100,"D":1000}
#List of indeces where each of the room are located
roomLocations = [2,4,6,8]
#Rooms we want to end up with
roomSolutuons = {2:"AA",4:"BB",6:"CC",8:"DD"}
#Dictionary that shows which is the home room for the given ahmphipod
homeRoom = {"A":0,"B":1,"C":2,"D":3}

#Priority queue of states - prioritiy determined by the energy cost
statesQueue = []
heapq.heappush(statesQueue,MyList([room1,room2,room3,room4,hallway,0]))
#Cache of seen states, where key is the string representation of the state, and the value is the minimum energy needed
#to reach that state
seenStates = dict()
seenStates[("".join(hallway)+room1+room2+room3+room4)] = 0

#Perform the Dijkstra until we hit the solution
while True:

    #Get the state with the lowest energy cost and expand that state
    s = heapq.heappop(statesQueue)

    #If we found the solution we are done
    if s[0] == roomSolutuons[2] and s[1] == roomSolutuons[4] and s[2] == roomSolutuons[6] and s[3] == roomSolutuons[8]:

        #Output
        print("The least energy required to organize the amphipods is :",s[-1])
        quit()


    #There are 2 things that can happen and change the state, first we can move amphipod from the room into the hallway
    #and second we can move amphipod from the halway to the room (but only to the room that is its home room)

    #Itarate over rooms
    for index in range(4):

        #Claculate the room index (2,4,6,8)
        roomLoc = 2+2*index

        #If room is empty or contains ONLY amphipods that belong to that room then do not move them to the hallway
        if roomSolutuons[roomLoc] == s[index]:
            continue
        if s[index] == "." + roomSolutuons[roomLoc][0]:
            continue
        if s[index] == "..":
            continue


        #Otherwise we can move top amphipod to the hallway
        #Calculate the position where we can move amphipod to
        #Starting with the place in the hallway where the room entrance is go left and right until we hit wall or
        #occupied place with another amphipod
        halwayStart = roomLoc
        halwayStop = roomLoc

        while halwayStart != 0 and s[4][halwayStart-1] == ".":
            halwayStart -= 1

        while halwayStop != 10 and s[4][halwayStop+1] == ".":
            halwayStop += 1

        #Now iterate over range where we can move amphipod to
        for h in range(halwayStart,halwayStop+1):
            #If the place is entrance to the room we cannot put it there
            #Otherwise move it to the current place and add that place to the prioritiy queue
            if h not in roomLocations:

                
                #Construct the new hallway state, new room state, and calculate the cost
                newCost = 0
                newHallway = s[4].copy()

                if s[index].startswith("."):
                    newHallway[h] = s[index][1]
                    newRoom = ".."
                    newCost += 2
                else:
                    newHallway[h] = s[index][0]
                    newRoom = "." + s[index][1]
                    newCost += 1

                newCost += abs(h-roomLoc)

                #For the cost we track the number of moves and then multiple it with correspoding factor
                newCost *= costToMove[newHallway[h]]

                #Construct the new state
                newState = s.copy()
                newState[index] = newRoom
                newState[4] = newHallway
                newState[5] += newCost

                #If the state has not yet been seen add it to the seen list and to the priority queue
                #If the state has already been seen, check if it has lower energy cost than the previosu one
                #If it does, then add it to the priority queue, otherwise ignore it
                stateString = "".join(newState[4])+newState[0]+newState[1]+newState[2]+newState[3]
                if stateString not in seenStates:
                    seenStates[stateString] = newState[5]
                    heapq.heappush(statesQueue,MyList(newState))
                elif newState[5] < seenStates[stateString]:
                    seenStates[stateString] = newState[5]
                    heapq.heappush(statesQueue,MyList(newState))


    #Now move every possible amhipod from the hallway to the room
    #Iterate over the hallway positions
    for index in range(hallwayLen):

        #If the position is empty just skip it
        if s[4][index] == ".":
            continue
        
        #Otherwise get the type of the amphipod on that position
        cur = s[4][index]

        #If that amhipod home roome is not empty or contains any amhipod that is different type
        #then we cannot move it to the room, otherwise try to move it to the room
        if s[homeRoom[cur]] not in ["..","."+cur]:
            continue
        
        #Copy the hallway and remove the amphipod on that position of the hallway
        newHallway = s[4].copy()
        newHallway[index] = "."
        #Find the range from the amhipod to its home room
        start,end = min(index,(homeRoom[cur]+1)*2),max(index,(homeRoom[cur]+1)*2)

        #Now check if all spaces in that range are empty
        #In other words, check if the amphipod can move to its home room
        canMove = True
        for loc in range(start,end+1):

            if newHallway[loc] != ".":
                canMove = False
                break

        #If it can move, move it 
        if canMove:

            #Create new state
            newState = s.copy()
            newCost = 0
            newState[4] = newHallway

            #Update room of the new state
            if newState[homeRoom[cur]] == "..":
                newRoom = "." + cur
                newCost += 2
            else:
                newCost += 1
                newRoom = cur + s[homeRoom[cur]][1]
            newState[homeRoom[cur]] = newRoom

            #Update cost of the new state
            newCost += end-start
            newState[5] += newCost * costToMove[cur]

            #If the state has not yet been seen add it to the seen list and to the priority queue
            #If the state has already been seen, check if it has lower energy cost than the previosu one
            #If it does, then add it to the priority queue, otherwise ignore it
            stateString = "".join(newState[4])+newState[0]+newState[1]+newState[2]+newState[3]
            if stateString not in seenStates:
                seenStates[stateString] = newState[5]
                heapq.heappush(statesQueue,MyList(newState))
            elif newState[5] < seenStates[stateString]:
                seenStates[stateString] = newState[5]
                heapq.heappush(statesQueue,MyList(newState))
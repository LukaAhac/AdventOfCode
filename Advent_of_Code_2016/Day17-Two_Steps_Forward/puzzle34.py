# ou're curious how robust this security solution really is, and so you decide to find longer 
# and longer paths which still provide access to the vault. You remember that paths always end 
# the first time they reach the bottom-right room (that is, they can never pass through it, only end in it).

# For example:

# If your passcode were ihgpwlah, the longest path would take 370 steps.
# With kglvqrro, the longest path would be 492 steps long.
# With ulqzkmiv, the longest path would be 830 steps long.
# What is the length of the longest path that reaches the vault?

#-----------------------------------------------------------------------------------------------------------

import hashlib

#Given data
data = "rrrbmfta"
xStart = 0
yStart = 0
xGoal = 3
yGoal = 3
openSigns = {"b","c","d","e","f"}

#Construct the first state (x,y,path)
allStates = [[xStart,yStart,""]]

#Variable for the longest path value
longestPath = 0

#Until we found solution
while True:

    #If there is no more states to process, terminate the loop
    if len(allStates) == 0:
        break

    #List of the next states
    nextStates = []

    #For each state in current iteration
    for state in allStates:

        #Check if it is a solution and discard it (since we cannot go further form that room)
        if state[0] == state[1] == 3:
            #If that solution had longer path then previously found, remember the length of it
            if len(state[2]) > longestPath:
                longestPath = len(state[2])
            continue

        #If not construct the passcode + path string
        stateString = data + state[2]
        #Compute the hash of it
        stateHash = hashlib.md5(stateString.encode()).hexdigest()

        #Check if up is open and if we can go up
        if stateHash[0] in openSigns and state[1] != 0:
            nextStates.append([state[0],state[1]-1,state[2]+"U"])
        #Check if down is open and  if we can go down
        if stateHash[1] in openSigns and state[1] != 3:
            nextStates.append([state[0],state[1]+1,state[2]+"D"])
        #Check if left is open and if we can go left
        if stateHash[2] in openSigns and state[0] != 0:
            nextStates.append([state[0]-1,state[1],state[2]+"L"])
        #Check if right is open and if we can go right
        if stateHash[3] in openSigns and state[0] != 3:
            nextStates.append([state[0]+1,state[1],state[2]+"R"])

    #States for next iteration
    allStates = nextStates

print("The length of the longest path that reaches the vault is:",longestPath)
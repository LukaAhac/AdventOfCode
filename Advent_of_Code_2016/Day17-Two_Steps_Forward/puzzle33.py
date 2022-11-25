# You're trying to access a secure vault protected by a 4x4 grid of small rooms connected by doors. 
# You start in the top-left room (marked S), and you can access the vault (marked V) once you reach the 
# bottom-right room:

# #########
# #S| | | #
# #-#-#-#-#
# # | | | #
# #-#-#-#-#
# # | | | #
# #-#-#-#-#
# # | | |  
# ####### V
# Fixed walls are marked with #, and doors are marked with - or |.

# The doors in your current room are either open or closed (and locked) based on the hexadecimal MD5 
# hash of a passcode (your puzzle input) followed by a sequence of uppercase characters representing 
# the path you have taken so far (U for up, D for down, L for left, and R for right).

# Only the first four characters of the hash are used; they represent, respectively, the doors up, down, 
# left, and right from your current position. Any b, c, d, e, or f means that the corresponding door is 
# open; any other character (any number or a) means that the corresponding door is closed and locked.

# To access the vault, all you need to do is reach the bottom-right room; reaching this room opens the 
# vault and all doors in the maze.

# For example, suppose the passcode is hijkl. Initially, you have taken no steps, and so your path is empty: 
# you simply find the MD5 hash of hijkl alone. The first four characters of this hash are ced9, which 
# indicate that up is open (c), down is open (e), left is open (d), and right is closed and locked (9). 
# Because you start in the top-left corner, there are no "up" or "left" doors to be open, so your only 
# choice is down.

# Next, having gone only one step (down, or D), you find the hash of hijklD. This produces f2bc, which 
# indicates that you can go back up, left (but that's a wall), or right. Going right means hashing hijklDR 
# to get 5745 - all doors closed and locked. However, going up instead is worthwhile: even though it returns 
# you to the room you started in, your path would then be DU, opening a different set of doors.

# After going DU (and then hashing hijklDU to get 528e), only the right door is open; after going DUR, 
# all doors lock. (Fortunately, your actual passcode is not hijkl).

# Passcodes actually used by Easter Bunny Vault Security do allow access to the vault if you know the 
# right path. For example:

# If your passcode were ihgpwlah, the shortest path would be DDRRRD.
# With kglvqrro, the shortest path would be DDUDRLRRUDRD.
# With ulqzkmiv, the shortest would be DRURDRUDDLLDLUURRDULRLDUUDDDRR.
# Given your vault's passcode, what is the shortest path (the actual path, not just the length) to 
# reach the vault?

# Your puzzle input is rrrbmfta.

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

#Until we found solution
while True:

    #List of the next states
    nextStates = []

    #For each state in current iteration
    for state in allStates:

        #Check if it is a solution
        if state[0] == state[1] == 3:
            print("The shortest path is:",state[2])
            quit()

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
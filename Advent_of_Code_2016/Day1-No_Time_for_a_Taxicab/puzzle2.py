# Then, you notice the instructions continue on the back of the Recruiting Document.
# Easter Bunny HQ is actually at the first location you visit twice.

# For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, 
# due East.

# How many blocks away is the first location you visit twice?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day1-No_Time_for_a_Taxicab\input.txt") as f:
    data = f.readlines()

#List of instructions
instructions = data[0].strip().split(", ")

#At the start we are facing North
facing_direction = "North"
#Our coordinates are (0,0)
x_cord = 0
y_cord = 0

#List of visited locations
visited_locations = []
#Old location
old_cords = (0,0)
found = False

#For each instruction move to instructed direction given number of steps
for index in range(len(instructions)):

    #If we are facing Norh
    if facing_direction == "North":

        #If instruction is R, now we are faceing East
        if instructions[index][0] == "R":

            facing_direction = "East"
            x_cord += int(instructions[index][1:])
        
        #If instrucion is L, now we are facing West
        elif instructions[index][0] == "L":

            facing_direction = "West"
            x_cord -= int(instructions[index][1:])

    #If we are facing East
    elif facing_direction == "East":

        #Righ is South
        if instructions[index][0] == "R":

            facing_direction = "South"
            y_cord -= int(instructions[index][1:])
        
        #Left is North
        elif instructions[index][0] == "L":

            facing_direction = "North"
            y_cord += int(instructions[index][1:])

    #Facing south
    elif facing_direction == "South":

        #Right is West
        if instructions[index][0] == "R":

            facing_direction = "West"
            x_cord -= int(instructions[index][1:])
        
        #Left is East
        elif instructions[index][0] == "L":

            facing_direction = "East"
            x_cord += int(instructions[index][1:])

    #Finally, if we are facing West
    elif facing_direction == "West":

        #Right is North
        if instructions[index][0] == "R":

            facing_direction = "North"
            y_cord += int(instructions[index][1:])
        
        #Left is South
        elif instructions[index][0] == "L":

            facing_direction = "South"
            y_cord -= int(instructions[index][1:])

    #New coordinates
    new_cords = (x_cord,y_cord)

    #If we were moving along Y axis
    if new_cords[0] == old_cords[0]:

        #If new Y is bigger than the old Y
        if new_cords[1] > old_cords[1]:

            #Make a list of blocks passed, but dont count the starting one because he is already covered before
            blocks = list(range(old_cords[1]+1,new_cords[1]+1))
        #If new Y is smaller than the old Y
        else:
            #Make a lsit of blocks passed, but dont count the starting one because he is alredy covered before
            blocks = list(range(new_cords[1],old_cords[1]))
            #Reverse the list
            blocks.reverse()

        #For each block
        for block in blocks:
            #Look if the block was already visited
            if (new_cords[0],block) in visited_locations:
                #If it is that is the HQ, we are done!
                HQ_loc = (new_cords[0],block)
                found = True
                break
            #If it is not, put it in the list of visited blocks
            else:
                visited_locations.append((new_cords[0],block))

    #If we were moving along X axis
    else:
        #If the new X is bigger than the old X
        if new_cords[0] > old_cords[0]:

            #Make a list of blocks passed, but dont count the starting one because he is already covered before
            blocks = list(range(old_cords[0]+1,new_cords[0]+1))
        #If the new X is smaller than the old X
        else:
            #Make a list of blocks passed, but dont count the starting one because he is already covered before
            blocks = list(range(new_cords[0],old_cords[0]))
            #Reverse the list
            blocks.reverse()

        #For each block
        for block in blocks:

            #Look if the block was already visited
            if (block,new_cords[1]) in visited_locations:
                #If it was, that is the HQ and we are done!
                HQ_loc = (block,new_cords[1])
                found = True
                break
            #Else add it to the list
            else:
                visited_locations.append((block,new_cords[1]))

    #If we found HQ dont loop more
    if found:
        break

    #Uppdate old cords for next iteration
    old_cords = new_cords

#Final distance is amount of blocks away from (0,0) in both X and Y direction from the found HQ
distance = abs(HQ_loc[0]) + abs(HQ_loc[1])

print("Easter Bunny HQ is", distance, "blocks away!")
# Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, 
# the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. 
# Each puzzle grants one star. Good luck!

# You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the 
# Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

# The Document indicates that you should start at the given coordinates (where you just landed) and face North. 
# Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

# There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. 
# Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

# For example:

# Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
# R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
# R5, L5, R5, R3 leaves you 12 blocks away.
# How many blocks away is Easter Bunny HQ?

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

#Final distance is amount of blocks away from (0,0) in both X and Y direction 
distance = abs(x_cord) + abs(y_cord)

print("Easter Bunny HQ is", distance, "blocks away!")
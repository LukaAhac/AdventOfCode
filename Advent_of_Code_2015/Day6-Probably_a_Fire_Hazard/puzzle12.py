# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

# The phrase turn on actually means that you should increase the brightness of those lights by 1.

# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

# The phrase toggle actually means that you should increase the brightness of those lights by 2.

# What is the total brightness of all lights combined after following Santa's instructions?

# For example:

# turn on 0,0 through 0,0 would increase the total brightness by 1.
# toggle 0,0 through 999,999 would increase the total brightness by 2000000.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day6-Probably_a_Fire_Hazard\input.txt") as f:
    data = f.readlines()

lights_grid = dict()

#Make the light grid as dictionary
for length in range(1000):
    for height in range(1000):
        lights_grid[str(length)+"--"+str(height)] = 0

#For each instruction
for instruction in data:
    splitted = instruction.strip().split()
    
    #If instruction is turn (on/off)
    if splitted[0].lower() == "turn":
        #Extract the coordinates
        start_x,start_y = splitted[2].split(",")
        end_x,end_y = splitted[-1].split(",")
        #Increase brightness
        if splitted[1].lower() == "on":
            for length in range(int(start_x), int(end_x)+1):
                for height in range(int(start_y), int(end_y)+1):
                    lights_grid[str(length)+"--"+str(height)] += 1
        #Decrease brightness
        elif splitted[1].lower() == "off":
            for length in range(int(start_x), int(end_x)+1):
                for height in range(int(start_y), int(end_y)+1):
                    if lights_grid[str(length)+"--"+str(height)] > 0:
                        lights_grid[str(length)+"--"+str(height)] -= 1
    #Increase brightness even more
    elif splitted[0].lower() == "toggle":
        #Extract the coordinates
        start_x,start_y = splitted[1].split(",")
        end_x,end_y = splitted[-1].split(",")
        #Toggle
        for length in range(int(start_x), int(end_x)+1):
            for height in range(int(start_y), int(end_y)+1):
                lights_grid[str(length)+"--"+str(height)] += 2


brightness = 0

#Count the total brightness
for length in range(1000):
    for height in range(1000):
        brightness += lights_grid[str(length)+"--"+str(height)]

print("The total brightness is {}.".format(brightness))
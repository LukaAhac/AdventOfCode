# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day6-Probably_a_Fire_Hazard\input.txt") as f:
    data = f.readlines()

lights_grid = dict()

#Make the light grid as dictionary
for length in range(1000):
    for height in range(1000):
        lights_grid[str(length)+"--"+str(height)] = False

#For each instruction
for instruction in data:
    splitted = instruction.strip().split()
    
    #If instruction is turn (on/off)
    if splitted[0].lower() == "turn":
        #Extract the coordinates
        start_x,start_y = splitted[2].split(",")
        end_x,end_y = splitted[-1].split(",")
        #Turn on
        if splitted[1].lower() == "on":
            for length in range(int(start_x), int(end_x)+1):
                for height in range(int(start_y), int(end_y)+1):
                    lights_grid[str(length)+"--"+str(height)] = True
        #Turn off
        elif splitted[1].lower() == "off":
            for length in range(int(start_x), int(end_x)+1):
                for height in range(int(start_y), int(end_y)+1):
                    lights_grid[str(length)+"--"+str(height)] = False
    #If instruction is toggle
    elif splitted[0].lower() == "toggle":
        #Extract the coordinates
        start_x,start_y = splitted[1].split(",")
        end_x,end_y = splitted[-1].split(",")
        #Toggle
        for length in range(int(start_x), int(end_x)+1):
            for height in range(int(start_y), int(end_y)+1):
                if lights_grid[str(length)+"--"+str(height)] == True:
                    lights_grid[str(length)+"--"+str(height)] = False
                else:
                    lights_grid[str(length)+"--"+str(height)] = True

lighted = 0

#Count how many lights are lit
for length in range(1000):
    for height in range(1000):
        if lights_grid[str(length)+"--"+str(height)] == True:
            lighted += 1

print(lighted,"lights are lit.")
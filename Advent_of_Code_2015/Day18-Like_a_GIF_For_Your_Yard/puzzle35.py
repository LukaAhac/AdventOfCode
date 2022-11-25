# After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

# Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

# Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

# Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) 
# depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have 
# fewer than eight neighbors; the missing ones always count as "off".

# For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has 
# the neighbors marked 1 through 5:

# 1B5...
# 234...
# ......
# ..123.
# ..8A4.
# ..765.
# The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

# A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
# A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
# All of the lights update simultaneously; they all consider the same current state before moving to the next.

# Here's a few steps from an example configuration of another 6x6 grid:

# Initial state:
# .#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####..

# After 1 step:
# ..##..
# ..##.#
# ...##.
# ......
# #.....
# #.##..

# After 2 steps:
# ..###.
# ......
# ..###.
# ......
# .#....
# .#....

# After 3 steps:
# ...#..
# ......
# ...#..
# ..##..
# ......
# ......

# After 4 steps:
# ......
# ......
# ..##..
# ..##..
# ......
# ......
# After 4 steps, this example has four lights on.

# In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day18-Like_a_GIF_For_Your_Yard\input.txt") as f:
    data = f.readlines()
    
#Number of light changes
steps = 100
#Dictionary that represents light grid
light_grid = dict()
#Row of lights
row = 0

#For each row of lights in data
for light_row in data:

    #Split row into columns
    lights_in_row = list(light_row.strip())
    #For each column
    for column in range(len(lights_in_row)):
        #Transform "#"" to 1 and save it to dictionary
        if lights_in_row[column] == "#":
            light_grid[(row,column)] = 1
        #Transform "." to 0 and save it to dictionary
        else:
            light_grid[(row,column)] = 0

    #Increase row
    row += 1

#For each step change lights
for _ in range(steps):

    #Create a copy of a grid on which changes will be made
    new_light_grid = light_grid.copy()

    #Fir each light
    for key in light_grid.keys():
        #Variable that tracks number of neighbours that are on
        lights_on = 0
        #For each light in a 3x3 box around current light
        for row in range(key[0]-1,key[0]+2):
            for column in range(key[1]-1,key[1]+2):
                #If it light exists (Lights in corners and first/lst row/column dont have equal amount of neighbour as other lights)
                if (row,column) in light_grid:
                    #Sum value of light (Light that is turned on has value of 1, and if it is turend off it has value of 0) 
                    lights_on += light_grid[(row,column)]

        #Remove self value from the sum
        lights_on -= light_grid[key]

        #Apply rules
        #If the light it turend on and it doenst have 2 or 3 lit neighbours
        if light_grid[key] == 1 and lights_on not in [2,3]:
            #Turn it off
            new_light_grid[key] = 0
        #If the light is turned off and it has 3 lit neighbours
        elif lights_on == 3:
            #Turn it on
            new_light_grid[key] = 1

    #Apply changes to the original grid
    light_grid = new_light_grid.copy()

#Variable to count lit lights
lights_on = 0

#Count lit liggts
for key in light_grid.keys():
    lights_on += light_grid[key]

print(lights_on,"lights are on after 100 steps")
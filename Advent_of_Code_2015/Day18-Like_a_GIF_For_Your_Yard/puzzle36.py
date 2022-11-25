# You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, 
# it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off. 
# The example above will actually run like this:

# Initial state:
# ##.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####.#

# After 1 step:
# #.##.#
# ####.#
# ...##.
# ......
# #...#.
# #.####

# After 2 steps:
# #..#.#
# #....#
# .#.##.
# ...##.
# .#..##
# ##.###

# After 3 steps:
# #...##
# ####.#
# ..##.#
# ......
# ##....
# ####.#

# After 4 steps:
# #.####
# #....#
# ...#..
# .##...
# #.....
# #.#..#

# After 5 steps:
# ##.###
# .##..#
# .##...
# .##...
# #.#...
# ##...#
# After 5 steps, this example now has 17 lights on.

# In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?

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

    #Turn on the corner lights
    light_grid[(0,0)] = 1
    light_grid[(0,(len(lights_in_row)-1))] = 1
    light_grid[((len(lights_in_row)-1),0)] = 1
    light_grid[((len(lights_in_row)-1),(len(lights_in_row)-1))] = 1

    #Increase row
    row += 1

#For each step change lights
for _ in range(steps):

    #Create a copy of a grid on which changes will be made
    new_light_grid = light_grid.copy()

    #Fir each light
    for key in light_grid.keys():
        #If it is one of the corner lights, skip it
        if key[0] == key[1] == 0:
            continue
        elif key[0] == 0 and key[1] == (len(lights_in_row)-1):
            continue
        elif key[0] == (len(lights_in_row)-1) and key[1] == 0:
            continue
        elif key[0] == key[1] == (len(lights_in_row)-1):
            continue

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

print(lights_on,"lights are on after 100 steps with the corners always on")
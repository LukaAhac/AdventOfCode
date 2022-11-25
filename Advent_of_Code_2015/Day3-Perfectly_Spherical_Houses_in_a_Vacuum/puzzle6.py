# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), 
# then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

# This year, how many houses receive at least one present?

# For example:

# ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
# ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
# ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------


#Read input
with open(r"Day3-Perfectly_Spherical_Houses_in_a_Vacuum\input.txt") as f:
    data = f.readlines()

#Input is one row
data = data[0]

santa_location = (0,0)
robo_santa_location = (0,0)
delivered = dict()
instruction_for = "Santa"

#Delivery to starting location
delivered[santa_location] = 2

#For each direction find new location
for direction in data:
    #Determine to which santa is direction given
    if instruction_for == "Santa":
        location = santa_location
    elif instruction_for == "Robo Santa":
        location = robo_santa_location

    if direction == "<":
        location = (location[0]-1,location[1])
    elif direction == ">":
        location = (location[0]+1,location[1])
    elif direction == "^":
        location = (location[0],location[1]+1)
    elif direction == "v":
        location = (location[0],location[1]-1)

    #Mark the deliver to that location
    if location in delivered:
        delivered[location] += 1
    else:
        delivered[location] = 1

    #Save new location for correct Santa and switch the flag
    if instruction_for == "Santa":
        santa_location = location
        instruction_for = "Robo Santa"
    elif instruction_for == "Robo Santa":
        robo_santa_location = location
        instruction_for = "Santa"
    

print("{} houses recieved at least one present".format(len(delivered.keys())))
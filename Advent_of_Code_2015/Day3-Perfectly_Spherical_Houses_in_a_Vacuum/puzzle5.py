# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. 
# Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. 
# How many houses receive at least one present?

# For example:

# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------


#Read input
with open(r"Day3-Perfectly_Spherical_Houses_in_a_Vacuum\input.txt") as f:
    data = f.readlines()

#Input is one row
data = data[0]

location = (0,0)
delivered = dict()

#Delivery to starting location
delivered[location] = 1

#For each direction find new location
for direction in data:
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
    

print("{} houses recieved at least one present".format(len(delivered.keys())))
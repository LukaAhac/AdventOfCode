# Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. 
# This must be a graphic design department; the walls are covered in specifications for triangles.

# Or are they?

# The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but 
# mark the impossible ones.

# In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, 
# because 5 + 10 is not larger than 25.

# In your puzzle input, how many of the listed triangles are possible?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day3-Squares_With_Three_Sides\input.txt") as f:
    data = f.readlines()

#List of triangle sides
triangles = []

for line in data:

    triangles.append(list(map(int,line.strip().split())))

#Possible triangle counter
possible_triangles = 0

#For each triangle check if the sum of each two sides is bigger than the third side
for triangle in triangles:

    if (triangle[0] + triangle[1]) > triangle[2] and (triangle[1] + triangle[2]) > triangle[0] and (triangle[2] + triangle[0]) > triangle[1]:

        possible_triangles += 1

print("There is {} possible triangles".format(possible_triangles))
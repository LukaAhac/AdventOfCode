# Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. 
# Each set of three numbers in a column specifies a triangle. Rows are unrelated.

# For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603
# In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day3-Squares_With_Three_Sides\input.txt") as f:
    data = f.readlines()

#List of triangle sides
triangles = []

#Go over three rows at once and store the triangles
for index in range(int(len(data)/3)):

    row1 = list(map(int,data[index*3].strip().split()))
    row2 = list(map(int,data[index*3+1].strip().split()))
    row3 = list(map(int,data[index*3+2].strip().split()))

    triangles.append([row1[0],row2[0],row3[0]])
    triangles.append([row1[1],row2[1],row3[1]])
    triangles.append([row1[2],row2[2],row3[2]])


#Possible triangle counter
possible_triangles = 0

#For each triangle check if the sum of each two sides is bigger than the third side
for triangle in triangles:

    if (triangle[0] + triangle[1]) > triangle[2] and (triangle[1] + triangle[2]) > triangle[0] and (triangle[2] + triangle[0]) > triangle[1]:

        possible_triangles += 1

print("There is {} possible triangles".format(possible_triangles))

# You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, 
# so it would be best to avoid them if possible.

# They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for 
# you to review. For example:

# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2
# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one 
# end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. 
# In other words:

# An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
# An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

# So, the horizontal and vertical lines from the above list would produce the following diagram:

# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....
# In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the 
# number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, 
# comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. 
# In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day5-Hydrothermal_Venture\input.txt") as f:
    data = f.readlines()

#Given input
inp = []

#Parse input
for line in data:
    line = line.strip().split()
    inp.append(line)

#Dictionary of points that vent pass through
points = dict()

#For each vent mark it into points
for vent in inp:

    #Get the starting and ending coordinates
    x_start,y_start = list(map(int,vent[0].split(",")))
    x_end,y_end = list(map(int,vent[2].split(",")))

    #We are only interested in vertical or horizontal vents
    if x_start == x_end or y_start == y_end:

        #Swap starts and ends if starts are higher coordiantes
        if x_start > x_end:
            temp = x_end
            x_end = x_start
            x_start = temp

        if y_start > y_end:
            temp = y_end
            y_end = y_start
            y_start = temp

        #Iterate through coordinates
        for x_range in range(x_start,x_end+1):

            for y_range in range(y_start,y_end+1):

                #Coordinate key
                key = str(x_range) + "-" + str(y_range)
                #Mark the coordinate in the points diciontary
                if key in points:

                    points[key] += 1
                else:
                    points[key] = 1

#Counter for double crossing points
counter = 0
#Count points that two or more vents cross through
for key in points:

    if points[key] > 1:
        counter += 1

#Output
print("At {} points at least two lines overlap".format(counter))
# Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also 
# consider diagonal lines.

# Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, 
# vertical, or a diagonal line at exactly 45 degrees. In other words:

# An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
# An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
# Considering all lines from the above example would now produce the following diagram:

# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....
# You still need to determine the number of points where at least two lines overlap. In the above example, this is 
# still anywhere in the diagram with a 2 or larger - now a total of 12 points.

# Consider all of the lines. At how many points do at least two lines overlap?

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

    #Horizontal vents
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

    #Vertical vents
    if abs(x_end-x_start) == abs(y_start-y_end):

        #List of x coordinates that vent passes through
        if x_start>x_end:
            x_coords = list(range(x_end,x_start+1))
            x_coords.reverse()
        else:
            x_coords = list(range(x_start,x_end+1))
        #List of y coordiantes that went passes through
        if y_start>y_end:
            y_coords = list(range(y_end,y_start+1))
            y_coords.reverse()
        else:
            y_coords = list(range(y_start,y_end+1))

        #Mark the coordinates in points dict
        for x,y in zip(x_coords,y_coords):

            #Coordinate key
            key = str(x) + "-" + str(y)
            #Mark the coordinate
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
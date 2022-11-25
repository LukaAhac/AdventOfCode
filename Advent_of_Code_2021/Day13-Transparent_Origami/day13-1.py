# You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal 
# imaging so you could tell ahead of time which caves are too hot to safely enter.

# Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

# Congratulations on your purchase! To activate this infrared thermal imaging
# camera system, please enter the code found on page 1 of the manual.
# Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go 
# to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with 
# random dots and includes instructions on how to fold it up (your puzzle input). For example:

# 6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0

# fold along y=7
# fold along x=5
# The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. 
# The first value, x, increases to the right. The second value, y, increases downward. So, the coordinate 
# 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form 
# the following pattern, where # is a dot on the paper and . is an empty, unmarked position:

# ...#..#..#.
# ....#......
# ...........
# #..........
# ...#....#.#
# ...........
# ...........
# ...........
# ...........
# ...........
# .#....#.##.
# ....#......
# ......#...#
# #..........
# #.#........
# Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper 
# and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). 
# In this example, the first fold instruction is fold along y=7, which designates the line formed by all 
# of the positions where y is 7 (marked here with -):

# ...#..#..#.
# ....#......
# ...........
# #..........
# ...#....#.#
# ...........
# ...........
# -----------
# ...........
# ...........
# .#....#.##.
# ....#......
# ......#...#
# #..........
# #.#........
# Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping 
# after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this 
# fold looks like this:

# #.##..#..#.
# #...#......
# ......#...#
# #...#......
# .#.#..#.###
# ...........
# ...........
# Now, only 17 dots are visible.

# Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after 
# the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is 
# transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen 
# through the transparent paper.

# Also notice that some dots can end up overlapping; in this case, the dots merge together and 
# become a single dot.

# The second fold instruction is fold along x=5, which indicates this line:

# #.##.|#..#.
# #...#|.....
# .....|#...#
# #...#|.....
# .#.#.|#.###
# .....|.....
# .....|.....
# Because this is a vertical line, fold left:

# #####
# #...#
# #...#
# #...#
# #####
# .....
# .....
# The instructions made a square!

# The transparent paper is pretty big, so for now, focus on just completing the first fold. 
# After the first fold in the example above, 17 dots are visible - dots that end up overlapping after 
# the fold is completed count as a single dot.

# How many dots are visible after completing just the first fold instruction on your transparent paper?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day13-Transparent_Origami\input.txt") as f:
    data = f.readlines()

#Given input
ins = []
dots = []

xMax = 0
yMax = 0

#Parse input
for line in data:
    line = line.strip().split()

    if len(line) == 1:

        line = line[0]
        line = line.split(",")
        line = list(map(int,line))

        if line[0] > xMax:
            xMax = line[0]
        if line[1] > yMax:
            yMax = line[1]

        dots.append(line)

    elif len(line) == 3:

        ins.append(line)

#Increase for easier looping
xMax += 1
yMax += 1

row = []

#Construct the paper with unique strings
for x in range(xMax):

    row.append(".")

paper = []

for y in range(yMax):

    paper.append(row.copy())

#Mark the dots
for d in dots:

    x,y = d
    paper[y][x] = "#"

#Perform foldings
#Folding is performd by reflecting the dots that are positioned after the folding axis
#to the other side of the axis such that their distance to the axis remains the same
#We also need to update the max x/y value after folding, and also keep half of the paper
for f in ins:

    #Get folding axis and itsvalue
    foldingAT = int(f[2].split("=")[1])
    foldingAlong = f[2].split("=")[0]

    #Fold along x axis
    if foldingAlong == "x":

        for x in range(foldingAT+1,xMax):

            for y in range(yMax):

                if x > foldingAT and paper[y][x] == "#":

                    dx = x-foldingAT

                    paper[y][foldingAT-dx] = "#"

        xMax = foldingAT

        for y in range(yMax):

            paper[y] = paper[y][:xMax]

    #Fold along y axos
    elif foldingAlong == "y":

        for x in range(xMax):

            for y in range(yMax):

                if y > foldingAT and paper[y][x] == "#":

                    dy = y-foldingAT

                    paper[foldingAT-dy][x] = "#"

        paper = paper[:foldingAT]
        yMax = foldingAT
    
    #Break because task 1 requries only one folding
    break

#Count the number of dots
counter = 0

for x in range(xMax):

    for y in range(yMax):

        if paper[y][x] == "#":
            counter += 1

print(counter,"dots are visible after completing just the first fold instruction on transparent paper.")

# Finish folding the transparent paper according to the instructions. 
# The manual says the code is always eight capital letters.

# What code do you use to activate the infrared thermal imaging camera system?

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


#Print the paper

print("The code to activate the infrared thermal imaging camera system is: \n")
for y in range(yMax):

    for x in range(xMax):

        if paper[y][x] != "#":
            print(" ",end = "")
        else:
            print("#",end = "")

    print("")
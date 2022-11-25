# You still can't quite make out the details in the image. Maybe you just didn't enhance it enough.

# If you enhance the starting input image in the above example a total of 50 times, 3351 pixels are lit 
# in the final output image.

# Start again with the original input image and apply the image enhancement algorithm 50 times. 
# How many pixels are lit in the resulting image?

#----------------------------------------------------------------------------------------------------------------------

import copy

#Read input
with open(r"Day20-Trench_Map\input.txt") as f:
    data = f.readlines()
    
#Given input
inp = []

#Parse input
for line in data:
    line = line.strip()
    inp.append(line)

#First line is image enchantinh algorithm
IEA = inp[0]

#The rest is the starting image
inp = inp[2:]

#Amount to append in each direction
app = 50
#Number of iteratiosn given in task
iterations = 50

#Constrcut the image with appendings
imageGrid = []

#Append top
for _ in range(app):

    imageGrid.append(["."]*(2*app+len(inp[0])))


#Append given rows left and right
for row in inp:

    newRow = ["."] * app
    newRow += row
    newRow += ["."] * app
    
    imageGrid.append(newRow)

#Append bottom
for _ in range(app):
    
    imageGrid.append(["."]*(2*app+len(inp[0])))

#Construct the empty grid with the same size
emptyGrid = [["." for _ in range(len(imageGrid[0]))] for _ in range(len(imageGrid))]

#Pixels that are in infinte - due to index for "........." begin "#" and index for "#########" being "."
#Each iteration whole inifinte grid will swap between "." and "#"
#This variable tracks what are the current pixels in infinte positions
pixelsInInf = "."

#Apply algorithm given number of times
for _ in range(iterations):

    newGrid = copy.deepcopy(emptyGrid)

    #Calculate the value of a pixel
    for row in range(len(imageGrid)):

        for column in range(len(imageGrid[0])):

            #Get the 3x3 grid around the current pixel representation
            numberString = ""

            for i1 in range(-1,2):

                for i2 in range(-1,2):

                    r = row+i1
                    c = column+i2

                    #If we re looking for a pixel out of the tracking grid, apply the pixel that are in infinte
                    if r < 0 or c < 0 or r >= len(imageGrid) or c >= len(imageGrid[0]):
                        numberString += pixelsInInf
                    else:
                        numberString += imageGrid[r][c]

            #Convert into bits
            numberString = numberString.replace(".","0")
            numberString = numberString.replace("#","1")
            #Bit to int
            number = int(numberString,2)

            #Replace the pixel with the one with calculated index in image enhancment algortihm
            newGrid[row][column] = IEA[number]

    #Calculate the new infinte pixel, which is always surrounded with other infinte pixels
    infNumber = [pixelsInInf]*9
    infNumber = "".join(infNumber)
    infNumber = infNumber.replace(".","0")
    infNumber = infNumber.replace("#","1")
    infNumber = int(infNumber,2)
    pixelsInInf = IEA[infNumber]

    imageGrid = copy.deepcopy(newGrid)


#Count the #
counter = 0

for row in imageGrid:

    for columnt in row:

        if columnt == "#":
            counter += 1

print(counter,"pixels are lit in result image.")
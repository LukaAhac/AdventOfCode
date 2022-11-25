# Sometimes, it's a good idea to appreciate just how big the ocean is. Using the Manhattan distance, 
# how far apart do the scanners get?

# In the above example, scanners 2 (1105,-1205,1229) and 3 (-92,-2380,-20) are the largest Manhattan distance apart. 
# In total, they are 1197 + 1175 + 1249 = 3621 units apart.

# What is the largest Manhattan distance between any two scanners?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day19-Beacon_Scanner\input.txt") as f:
    data = f.readlines()
    
#Given input
scanerReadings = dict()

#Parse input
for line in data:
    line = line.strip()
    if line.startswith("---"):
        key = line[4:-4]
    elif line:
        line = line.split(",")
        if key in scanerReadings:
            scanerReadings[key].append((int(line[0]),int(line[1]),int(line[2])))
        else:
            scanerReadings[key] = [(int(line[0]),int(line[1]),int(line[2]))]

scannerReadingsCopy = scanerReadings.copy()

#Dictionary of solved scaners as keys and their coordinates and rotations as values
solvedScanners = dict()
#We are looking everything in realtion to the scanner 0
solvedScanners["scanner 0"] = (0,0,0,"x","y")

#Function that rotates the given point for given axises
#Returns the rotated point
def rotatePoint(point,x,y):

    rotatedPoint = [0,0,0]
    zIndex = [0,1,2]

    #Get x
    if x == "x":
        rotatedPoint[0] = point[0]
        zIndex.remove(0)
    elif x == "-x":
        rotatedPoint[0] = -point[0]
        zIndex.remove(0)
    elif x == "y":
        rotatedPoint[0] = point[1]
        zIndex.remove(1)
    elif x == "-y":
        rotatedPoint[0] = -point[1]
        zIndex.remove(1)
    elif x == "z":
        rotatedPoint[0] = point[2]
        zIndex.remove(2)
    elif x == "-z":
        rotatedPoint[0] = - point[2]
        zIndex.remove(2)

    #Get y
    if y == "x":
        rotatedPoint[1] = point[0]
        zIndex.remove(0)
    elif y == "-x":
        rotatedPoint[1] = -point[0]
        zIndex.remove(0)
    elif y == "y":
        rotatedPoint[1] = point[1]
        zIndex.remove(1)
    elif y == "-y":
        rotatedPoint[1] = -point[1]
        zIndex.remove(1)
    elif y == "z":
        rotatedPoint[1] = point[2]
        zIndex.remove(2)
    elif y == "-z":
        rotatedPoint[1] = - point[2]
        zIndex.remove(2)

    #Get z
    #z is defined with x and y, those 12 combinations are done manually - YOU SHOULD NOT DO IT THIS WAY
    if (x == "x" and y == "y") or (x == "y" and y == "-x") or (x == "-x" and y == "-y") or (x == "-y" and y == "x") \
        or (x == "-z" and y == "y") or (x == "y" and y == "z") or (x == "z" and y == "-y") or (x == "-y" and y == "-z") \
        or (x == "-z" and y == "-x") or ( x == "x" and y == "-z") or (x == "z" and y == "x") or (x == "-x" and y == "z"):

        rotatedPoint[2] = point[zIndex[0]]
        z = "+"
    else:
        rotatedPoint[2] = -point[zIndex[0]]
        z = "-"

    return rotatedPoint




#Until all scanres are solved
while len(solvedScanners.keys()) != len(scanerReadings.keys()):

    #Flag to exit multiple loops if we solve a scanner coords
    doneWithThis = False

    newSolved = solvedScanners.copy()


    #We can only solve one by matching it with already solved one
    for key in solvedScanners.keys():

        if doneWithThis:
            break

        for keyUnsolved in scanerReadings.keys():

            if doneWithThis:
                break

            #If we are matching two solved ones, continue
            if keyUnsolved in solvedScanners.keys():
                continue

            #Do 24 rotations
            #First we are chosing where are we going to put x axis
            #And we can put it alongise any of the 3D axis (X,Y,Z) and then we can put it in 
            #either direction for those axis, therfore we can put x axis in 3x2 = 6 ways
            #After we pick one axis for an x, the remaining two axis are left to put y on either of them
            for x in ["x","-x","y","-y","z","-z"]:

                if x[-1] == "x":
                    possibleY = ["y","-y","z","-z"]
                elif x[-1] == "y":
                    possibleY = ["x","-x","z","-z"]
                else:
                    possibleY = ["x","-x","y","-y"]

                if doneWithThis:
                    break

                #There are 2 left axis to put y on, and we can put y axis in either direction on those two axis
                #therfore, there are 2x2 = 4 ways to put y axis
                #After chooinsg both x and y, z axis is defined aswell, because there is only one axis it can go to
                #and there is only one direction it can go to while coordainte system being valid
                for y in possibleY:

                    if doneWithThis:
                        break

                    #Rotate each point with current rotation
                    transformedReadings = []

                    for reading2 in scanerReadings[keyUnsolved]:

                        r2 = rotatePoint(reading2,x,y)
                        transformedReadings.append(r2)


                    #Try to mach every point in solved scanner with every rotated point in unsolved scanner
                    xOffsets = dict()
                    yOffsets = dict()
                    zOffsets = dict()

                    for reading1 in scanerReadings[key]:

                        for reading2 in transformedReadings:

                            x_diff = reading1[0]-reading2[0]
                            y_diff = reading1[1]-reading2[1]
                            z_diff = reading1[2]-reading2[2]

                            if x_diff in xOffsets:
                                xOffsets[x_diff] += 1
                            else:
                                xOffsets[x_diff] = 1
                            
                            if y_diff in yOffsets:
                                yOffsets[y_diff] += 1
                            else:
                                yOffsets[y_diff] = 1

                            if z_diff in zOffsets:
                                zOffsets[z_diff] += 1
                            else:
                                zOffsets[z_diff] = 1

                    #If there are more then 12 matches for EACH of the axis then we can calculat the position
                    #of the unsovled scanner - postion will be relative distance to the solved scanner + solved
                    #scanner distane to the (0,0,0)
                    f1 = f2 = f3 = False

                    scannerCords = [0,0,0]

                    for offsetKey in xOffsets.keys():

                        if xOffsets[offsetKey] >= 12:
                            f1 = True
                            scannerCords[0] = offsetKey + solvedScanners[key][0]
                    
                    for offsetKey in yOffsets.keys():

                        if yOffsets[offsetKey] >= 12:
                            #print(offsetKey,yOffsets[offsetKey],"Y")
                            f2 = True
                            scannerCords[1] = offsetKey + solvedScanners[key][1]

                    for offsetKey in zOffsets.keys():

                        if zOffsets[offsetKey] >= 12:
                            #print(offsetKey,zOffsets[offsetKey],"Z")
                            f3 = True
                            scannerCords[2] = offsetKey + solvedScanners[key][2]
                    
                    #If we managed to solve it, mark as solved and go to the next scanner
                    if f1 and f2 and f3:
                        scannerCords.append(x)
                        scannerCords.append(y)
                        newSolved[keyUnsolved] = scannerCords
                        scanerReadings[keyUnsolved] = transformedReadings
                        doneWithThis = True

    solvedScanners = newSolved


#Calculate distance between every 2 scanners
distances = []

for scanner1 in solvedScanners.values():
    
    for scanner2 in solvedScanners.values():

        dis = abs(scanner1[0]-scanner2[0]) + abs(scanner1[1]-scanner2[1]) + abs(scanner1[2]-scanner2[2])
        distances.append(dis)


print("The largest Manhattan distance between any two scanners is:",max(distances))
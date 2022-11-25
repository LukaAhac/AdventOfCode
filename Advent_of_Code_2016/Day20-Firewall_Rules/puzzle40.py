# How many IPs are allowed by the blacklist?

#-----------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day20-Firewall_Rules\input.txt") as f:
    data = f.readlines()

#List of the blokced ranges -> INPUT
blockedRanges = []
#Fetch the ranges from the input
for line in data:
    line = line.strip().split("-")
    blockedRanges.append((int(line[0]),int(line[1])))
#IP range given in task
firstIp = 0
lastIp = 4294967295

#Put the whole range as valid at the start
validIpRanges =  [[firstIp,lastIp]]

#For each blocked range, remove it from the valid ranges
for blockedRange in blockedRanges:

    #Bounds of the blocked range
    lowerBound = blockedRange[0]
    upperBound = blockedRange[1]

    #Flag that indicates wheter or not indexes are found
    lowerIndexFound = False
    upperIndexFound = False
    #Flags that detects wheter or not the blocked bounds are contained within valid ranges
    lowerBoundInValidRange = False
    upperBoundInValidRange = False
    #Index of the valid range that is left to a blocked bound or contains a blocked bound 
    indexForLowerBound = 0
    indexForUpperBound = 0

    #Search for the indexes
    for index in range(len(validIpRanges)):

        #If we found the indexes terminate the search
        if lowerIndexFound and upperIndexFound:
            break

        #Current IP range that we are searching on
        currentIp = validIpRanges[index]
        
        #If lower index not found
        if not lowerIndexFound:

            #If the lower bound is bigger than the current range remember the range and go to the next one
            if lowerBound > currentIp[0] and lowerBound > currentIp[1]:
                indexForLowerBound = index
            #If the lower bound is lower than the current range, we remember the last range and we are done
            elif lowerBound < currentIp[0]:
                lowerIndexFound = True
            #If the lower bound is withn the current range remember the range and mark the flags
            elif lowerBound >= currentIp[0] and lowerBound <= currentIp[1]:
                indexForLowerBound = index
                lowerBoundInValidRange = True
                lowerIndexFound = True
            

        if not upperIndexFound:

            #If the upper bound is bigger than the current range remember the range and go to the next one
            if upperBound > currentIp[0] and upperBound > currentIp[1]:
                indexForUpperBound = index
            #If the upper bound is lower then the current range, we remember the last range and we are done
            elif upperBound < currentIp[0]:
                upperIndexFound = True
            #If the upper bound is within the ucrrent range, remember the range and mark the flags
            elif upperBound >= currentIp[0] and upperBound <= currentIp[1]:
                indexForUpperBound = index
                upperBoundInValidRange = True
                upperIndexFound = True

    #Case 1: both bounds are within the valid ranges
    if lowerBoundInValidRange and upperBoundInValidRange:

        #Case 1.1 both bounds are within the same range -> split it into two ranges
        if indexForLowerBound == indexForUpperBound:
            #Range that they are within
            withinRange = validIpRanges[indexForUpperBound]

            #Create new ranges
            newRange1 = [withinRange[0],lowerBound-1]
            newRange2 = [upperBound+1,withinRange[1]]

            #Replace the current range with the lower one
            validIpRanges[indexForLowerBound] = newRange1
            #Insert the bigger range after the lower one
            validIpRanges.insert(indexForLowerBound+1,newRange2)

            #If any of the two new ranges are invalid (happens if either of the range bounds were
            #equal to the f valid range bounds)
            if validIpRanges[indexForLowerBound+1][0] > validIpRanges[indexForLowerBound+1][1]:
                del validIpRanges[indexForLowerBound+1]
            if validIpRanges[indexForLowerBound][0] > validIpRanges[indexForLowerBound][1]:
                del validIpRanges[indexForLowerBound]
        #Case 1.2 bounds are not within the same range
        else:
            
            #Move the valid range lower bound to match the upper bound (+1) of the invalid range
            validIpRanges[indexForUpperBound][0] = upperBound+1
            #Move the valid range upper bound to match the lower bound (-1) of the invalid range
            validIpRanges[indexForLowerBound][1] = lowerBound-1

            #If the higher range became invalid, delete it
            if validIpRanges[indexForUpperBound][0] > validIpRanges[indexForUpperBound][1]:
                del validIpRanges[indexForUpperBound]
            #Delete all the ranges that where inbetween two ranges where invalid ranges bounds ended up
            rangesToDelete = indexForUpperBound-indexForLowerBound-1
            for _ in range(rangesToDelete):
                del validIpRanges[indexForLowerBound+1]
            #If the lower range became invalid, delete it
            if validIpRanges[indexForLowerBound][0] > validIpRanges[indexForLowerBound][1]:
                del validIpRanges[indexForLowerBound]

    #Case 2: lower bound is not in the valid range and upper bound is in the valid range
    if not lowerBoundInValidRange and upperBoundInValidRange:

        #Move the valid range lower bound to match the upper bound (+1) of the invalid range
        validIpRanges[indexForUpperBound][0] = upperBound + 1
        #If it became invalid, delete it
        if validIpRanges[indexForUpperBound][0] > validIpRanges[indexForUpperBound][1]:
            del validIpRanges[indexForUpperBound]

        #Delete all the ranges that where inbetween
        rangesToDelete = indexForUpperBound - indexForLowerBound - 1
        for _ in range(rangesToDelete):
            del validIpRanges[indexForLowerBound+1]

    #Case 3: lowe bound is in the valid range and upper bound is not in the valid range
    if lowerBoundInValidRange and not upperBoundInValidRange:

        #Move the valid range upper bound to match the lower bound (-1) of the invalid range
        validIpRanges[indexForLowerBound][1] = lowerBound - 1
        #Delete all the ranges that where inbetween, this time not -1 because we always have
        #the index of the valid block that is left to the bound or contains the bound
        rangesToDelete = indexForUpperBound - indexForLowerBound
        for _ in range(rangesToDelete):
            del validIpRanges[indexForLowerBound+1]
        #If the lower bound range became invalid, delite it
        if validIpRanges[indexForLowerBound][0] > validIpRanges[indexForLowerBound][1]:
            del validIpRanges[indexForLowerBound]
    
    #Case 4: both bounds are not within valid ranges
    if not lowerBoundInValidRange  and not upperBoundInValidRange:

        #Just delete the ranges that are between them (if there are any)
        rangesToDelete = indexForUpperBound - indexForLowerBound
        for _ in range(rangesToDelete):
            del validIpRanges[indexForLowerBound+1]

allowedIPs = 0

for validRange in validIpRanges:

    allowedIPs += validRange[1] - validRange[0] + 1

print(allowedIPs,"IPs are allowed by the blacklist")
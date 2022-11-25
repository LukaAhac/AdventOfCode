# It seems like the individual flashes aren't bright enough to navigate. However, you might 
# have a better option: the flashes seem to be synchronizing!

# In the example above, the first time all octopuses flash simultaneously is step 195:

# After step 193:
# 5877777777
# 8877777777
# 7777777777
# 7777777777
# 7777777777
# 7777777777
# 7777777777
# 7777777777
# 7777777777
# 7777777777

# After step 194:
# 6988888888
# 9988888888
# 8888888888
# 8888888888
# 8888888888
# 8888888888
# 8888888888
# 8888888888
# 8888888888
# 8888888888

# After step 195:
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# 0000000000
# If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be 
# able to navigate through the cavern. What is the first step during which all octopuses flash?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day11-Dumbo_Octopus\input.txt") as f:
    data = f.readlines()

#Given input
energy = []

#Parse input
for line in data:
    line = list(map(int,list(line.strip())))
    energy.append(line)

#Number of flashes
flashes = 0

#Steps that it takes for all of them to flash
steps = 0

#Count the flashes in frist 100 iteration
while True:

    steps += 1

    #Octopus can flash once per turn, so track flashes
    alreadyFlashed = [[False for _ in range(len(energy[0]))] for _ in range(len(energy))]
    #List of octopus that will flash
    toFlash = []

    #Increase energy by 1, add to list if it is about to flash
    for x in range(len(energy[0])):

        for y in range(len(energy)):

            energy[y][x] += 1

            if energy[y][x] > 9:

                toFlash.append((x,y))

    #Until there is no more to flash
    while len(toFlash) > 0:

        #Clear the lsit for the next iteration
        lastFlash = toFlash.copy()
        toFlash = []

        #For octopus that will flash
        for x,y in lastFlash:

            #If already flashed skip it
            if alreadyFlashed[y][x] == True:
                continue

            #Else flash it
            alreadyFlashed[y][x] = True
            flashes += 1

            #Increase energy for neighbour octopus
            moves = [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,0),(1,-1),(1,1)]

            for dx,dy in moves:

                newX = x+dx
                newY = y+dy

                if 0<=newX<len(energy[0])  and  0 <=newY<len(energy):

                    energy[newY][newX] += 1

                    #If they new energy exceed 9 and they did not flash, add them to the list for next iteration
                    if energy[newY][newX] > 9 and alreadyFlashed[newY][newX] is False:
                        toFlash.append((newX,newY))

    #Lastly, set the energy of those that flashed to 0, if all octopus flashed we are done
    allFlashed = True

    for x in range(len(energy[0])):

        for y in range(len(energy)):

            if energy[y][x] > 9:

                energy[y][x] = 0
            if alreadyFlashed[y][x] is False:
                allFlashed = False

    if allFlashed:
        break

print("The first step during which all octopus flash is :",steps)
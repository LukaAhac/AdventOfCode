# After getting the first capsule (it contained a star! what great fortune!), 
# the machine detects your success and begins to rearrange itself.

# When it's done, the discs are back in their original configuration as if it were time=0 again, 
# but a new disc with 11 positions and starting at position 0 has appeared exactly one second below 
# the previously-bottom disc.

# With this new disc, and counting again starting from time=0 with the configuration in your puzzle input, 
# what is the first time you can press the button to get another capsule?

#-----------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day15-Timing_is_Everything\input.txt") as f:
    data = f.readlines()

#Dictionary of discs
discs = dict()

#Retrive data for each disc
for line in data:
    line = line.strip().split()

    discs[line[1]] = (int(line[3]),int(line[-1][:-1]))

discs["#7"] = (11,0)

#Get the number of discs
numberOfDiscs = len(discs)
#We start from time = 0
currentTime = 0

#Until we find solution
while True:

    #Time where capsule reaches each disc
    discTime = currentTime
    #Numbers of dics that capsule passed through
    discPassed = 0

    #For each disc
    for disc in sorted(discs.keys()):

        #It takes a second to reach next disc
        discTime += 1

        #If disc is not at the position 0 at that time then thats is not the valid time to drop the capsule
        if ((discs[disc][1]+discTime) % discs[disc][0]) != 0:
            break
        
        #If the disc was at the position 0, capsule will pass the disc
        discPassed += 1

    #If the capsule passed all the discs, solution is found
    if discPassed == numberOfDiscs:
        break

    #If we did not find solution, go to the next time
    currentTime += 1

print("The first time you can press the button to get a capsule is:",currentTime)
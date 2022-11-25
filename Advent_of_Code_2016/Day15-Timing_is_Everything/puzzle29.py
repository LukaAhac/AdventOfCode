# he halls open into an interior plaza containing a large kinetic sculpture. 
# The sculpture is in a sealed enclosure and seems to involve a set of identical spherical capsules 
# that are carried to the top and allowed to bounce through the maze of spinning pieces.

# Part of the sculpture is even interactive! When a button is pressed, a capsule is dropped and 
# tries to fall through slots in a set of rotating discs to finally go through a little hole at 
# the bottom and come out of the sculpture. If any of the slots aren't aligned with the capsule as 
# it passes, the capsule bounces off the disc and soars away. You feel compelled to get one of those capsules.

# The discs pause their motion each second and come in different sizes; they seem to each have a 
# fixed number of positions at which they stop. You decide to call the position with the slot 0, 
# and count up for each position it reaches next.

# Furthermore, the discs are spaced out so that after you push the button, one second elapses 
# before the first disc is reached, and one second elapses as the capsule passes from one disc 
# to the one below it. So, if you push the button at time=100, then the capsule reaches the top disc 
# at time=101, the second disc at time=102, the third disc at time=103, and so on.

# The button will only drop a capsule at an integer time - no fractional seconds allowed.

# For example, at time=0, suppose you see the following arrangement:

# Disc #1 has 5 positions; at time=0, it is at position 4.
# Disc #2 has 2 positions; at time=0, it is at position 1.
# If you press the button exactly at time=0, the capsule would start to fall; it would reach the 
# first disc at time=1. Since the first disc was at position 4 at time=0, by time=1 it has ticked 
# one position forward. As a five-position disc, the next position is 0, and the capsule falls through the slot.

# Then, at time=2, the capsule reaches the second disc. The second disc has ticked forward two positions 
# at this point: it started at position 1, then continued to position 0, and finally ended up at position 
# 1 again. Because there's only a slot at position 0, the capsule bounces away.

# If, however, you wait until time=5 to push the button, then when the capsule reaches each disc,
# the first disc will have ticked forward 5+1 = 6 times (to position 0), and the second disc will 
# have ticked forward 5+2 = 7 times (also to position 0). In this case, the capsule would fall through 
# the discs and come out of the machine.

# However, your situation has more than two discs; you've noted their positions in your puzzle input. 
# What is the first time you can press the button to get a capsule?

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
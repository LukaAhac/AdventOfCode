# The crabs don't seem interested in your proposed solution. Perhaps you misunderstand crab engineering?

# As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 
# step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second 
# step costs 2, the third step costs 3, and so on.

# As each crab moves, moving further becomes more expensive. This changes the best horizontal position to 
# align them all on; in the example above, this becomes 5:

# Move from 16 to 5: 66 fuel
# Move from 1 to 5: 10 fuel
# Move from 2 to 5: 6 fuel
# Move from 0 to 5: 15 fuel
# Move from 4 to 5: 1 fuel
# Move from 2 to 5: 6 fuel
# Move from 7 to 5: 3 fuel
# Move from 1 to 5: 10 fuel
# Move from 2 to 5: 6 fuel
# Move from 14 to 5: 45 fuel
# This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2)
# now costs 206 fuel instead.

# Determine the horizontal position that the crabs can align to using the least fuel possible so they can 
# make you an escape route! How much fuel must they spend to align to that position?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day7-The_Treachery_of_Whales\input.txt") as f:
    data = f.readlines()

#Given input
inp = []

#Parse input
for line in data:
    line = line.strip()
    inp.append(line)

#We have only one line of input
inp = inp[0].split(",")
#Make it as integers
inp = list(map(int,inp))

#Find min and max in the input
x_min = min(inp)
x_max = max(inp)
#Cost of fuel for each position
costs = []

#Calculate the cost for each position
for position in range(x_min,x_max):

    #Initally cost is 0
    cost = 0

    #For each crab add its cost 
    for crab_position in inp:
        
        distance = abs(position-crab_position)

        #Cost is the number of steps between him and goal position
        cost += int(distance*(distance+1)/2)

    #Append the postion and the cost to the costs list
    costs.append([position,cost])

#Sort that list by the costs
costs = sorted(costs,key = lambda x:x[1])

print("They must spend {} fuel to align to that position!".format(costs[0][1]))
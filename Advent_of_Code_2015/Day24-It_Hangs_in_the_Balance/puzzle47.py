# It's Christmas Eve, and Santa is loading up the sleigh for this year's deliveries. However, there's one small problem: 
# he can't get the sleigh to balance. If it isn't balanced, he can't defy physics, and nobody gets presents this year.

# No pressure.

# Santa has provided you a list of the weights of every package he needs to fit on the sleigh. 
# The packages need to be split into three groups of exactly the same weight, and every package has to fit. 
# The first group goes in the passenger compartment of the sleigh, and the second and third go in containers on either side. 
# Only when all three groups weigh exactly the same amount will the sleigh be able to fly. Defying physics has rules, you know!

# Of course, that's not the only problem. The first group - the one going in the passenger compartment - needs as few packages as possible 
# so that Santa has some legroom left over. It doesn't matter how many packages are in either of the other two groups, so long as all of the groups weigh the same.

# Furthermore, Santa tells you, if there are multiple ways to arrange the packages such that the fewest possible are 
# in the first group, you need to choose the way where the first group has the smallest quantum entanglement to reduce the chance 
# of any "complications". The quantum entanglement of a group of packages is the product of their weights, that is, the value you get 
# when you multiply their weights together. Only consider quantum entanglement if the first group has the fewest possible number of packages 
# in it and all groups weigh the same amount.

# For example, suppose you have ten packages with weights 1 through 5 and 7 through 11. For this situation, some of the unique 
# first groups, their quantum entanglements, and a way to divide the remaining packages are as follows:

# Group 1;             Group 2; Group 3
# 11 9       (QE= 99); 10 8 2;  7 5 4 3 1
# 10 9 1     (QE= 90); 11 7 2;  8 5 4 3
# 10 8 2     (QE=160); 11 9;    7 5 4 3 1
# 10 7 3     (QE=210); 11 9;    8 5 4 2 1
# 10 5 4 1   (QE=200); 11 9;    8 7 3 2
# 10 5 3 2   (QE=300); 11 9;    8 7 4 1
# 10 4 3 2 1 (QE=240); 11 9;    8 7 5
# 9 8 3      (QE=216); 11 7 2;  10 5 4 1
# 9 7 4      (QE=252); 11 8 1;  10 5 3 2
# 9 5 4 2    (QE=360); 11 8 1;  10 7 3
# 8 7 5      (QE=280); 11 9;    10 4 3 2 1
# 8 5 4 3    (QE=480); 11 9;    10 7 2 1
# 7 5 4 3 1  (QE=420); 11 9;    10 8 2
# Of these, although 10 9 1 has the smallest quantum entanglement (90), the configuration with only two packages, 11 9, in the passenger 
# compartment gives Santa the most legroom and wins. In this situation, the quantum entanglement for the ideal configuration is therefore 99. 
# Had there been two configurations with only two packages in the first group, the one with the smaller quantum entanglement would be chosen.

# What is the quantum entanglement of the first group of packages in the ideal configuration?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

from math import prod

#Read input
with open(r"Day24-It_Hangs_in_the_Balance\input.txt") as f:
    data = f.readlines()

#Reverse data for better efficient
data.reverse()

#Variable that store weights
weights = []
#Load weights
for line in data:
    weights.append(int(line.strip()))

#Calculate teh weight that each group should have
group_weight = sum(weights)/3

#Variable that will store possible groups
possible_gorups = [[]]

#Calculate possible groups
for index in range(len(weights)):

    #Coppy discovered groups into the next step
    next_groups = possible_gorups.copy()

    #For each of already discovered group
    for group in possible_gorups:

        #Add new element to it if it wouldn't exceed required group weight
        if sum(group) + weights[index] <= group_weight:
            next_groups.append(group.copy())
            next_groups[-1].append(weights[index])

    #Carry discovered groups into next step
    possible_gorups = next_groups

#Variable that will hold groups that have required weight
valid_groups = []

#For each discovered group, cheack if it has required weight
for group in possible_gorups:

    #Save it as a SET if it does
    if sum(group) == group_weight:
        valid_groups.append(set(group))

#Sort groups by the number of elements they have - we are looking for group that has as little elements as possible
valid_groups = sorted(valid_groups, key = lambda x: len(x))

#Lowest lenght will be lenght of the first group
best_len = len(valid_groups[0])

#Do until you find solution
while True:

    #Variable to hold possible solution with lowest number of elements
    groups_with_best_len = []
    #Find all groups that have len same as required
    for group in valid_groups:

        if len(group) == best_len:

            groups_with_best_len.append(group)

    #Sort group by product - quantum entanglement
    groups_with_best_len = sorted(groups_with_best_len, key = lambda x: prod(x))

    #Flag that marks if solution is found
    found = False

    #Check if the group can form full set of weights with any other two disjoint groups
    for group in groups_with_best_len:

        no_intersection = []

        #For gorup that might be possible solution collect all disjoint valid groups
        for group2 in valid_groups:

            if len(group.intersection(group2)) == 0:

                no_intersection.append(group2)

        #Check if any two groups are disjoint - if they are that means that we can form full set of weight with those two and solution group
        for index1 in range(len(no_intersection)):

            for index2 in range(index1+1,len(no_intersection)):

                if len(no_intersection[index1].intersection(no_intersection[index2])) == 0:
                    
                    #If two disjoint groups are found break all loops becuase we have solution
                    found = True
                    break
            if found:
                break

        if found:
            break
    if found:
        break

    #If solution is not found with that len increse it and look again
    if best_len < len(valid_groups[-1]):
        best_len += 1

print("Quantum entanglement of the first group of packages in the ideal configuration is",prod(group))

# That's weird... the sleigh still isn't balancing.

# "Ho ho ho", Santa muses to himself. "I forgot the trunk".

# Balance the sleigh again, but this time, separate the packages into four groups instead of three. The other constraints still apply.

# Given the example packages above, this would be some of the new unique first groups, their quantum entanglements, and one way to divide the remaining packages:


# 11 4    (QE=44); 10 5;   9 3 2 1; 8 7
# 10 5    (QE=50); 11 4;   9 3 2 1; 8 7
# 9 5 1   (QE=45); 11 4;   10 3 2;  8 7
# 9 4 2   (QE=72); 11 3 1; 10 5;    8 7
# 9 3 2 1 (QE=54); 11 4;   10 5;    8 7
# 8 7     (QE=56); 11 4;   10 5;    9 3 2 1
# Of these, there are three arrangements that put the minimum (two) number of packages in the first group: 11 4, 10 5, and 8 7. 
# Of these, 11 4 has the lowest quantum entanglement, and so it is selected.

# Now, what is the quantum entanglement of the first group of packages in the ideal configuration?

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
group_weight = sum(weights)/4

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

    #Check if the group can form full set of weights with any other three disjoint groups
    for group in groups_with_best_len:

        no_intersection = []

        #For gorup that might be possible solution collect all disjoint valid groups
        for group2 in valid_groups:

            if len(group.intersection(group2)) == 0:

                no_intersection.append(group2)

        #Check if any three groups are disjoint - if they are that means that we can form full set of weight with those three and solution group
        for index1 in range(len(no_intersection)):

            for index2 in range(index1+1,len(no_intersection)):

                for index3 in range(index2+1,len(no_intersection)):

                    if len(no_intersection[index1].intersection(no_intersection[index2],no_intersection[index3])) == 0:

                            #If three disjoint groups are found break all loops becuase we have solution
                        found = True
                        break
                    if found:
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
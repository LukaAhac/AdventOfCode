# Every year, Santa manages to deliver all of his presents in a single night.

# This year, however, he has some new locations to visit; his elves have provided him the distances between
# every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. 
# What is the shortest distance he can travel to achieve this?

# For example, given the following distances:

# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# The possible routes are therefore:

# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982
# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

# What is the distance of the shortest route?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

import itertools

#Read input
with open(r"Day9-All_in_a_Single_Night\input.txt") as f:
    data = f.readlines()

distances = dict()
towns = set()

#For each distance
for distance in data:

    splitted = distance.strip().split()

    #Save the distance into the dictionary
    distances[splitted[0]+"->"+splitted[2]] = int(splitted[4])
    #Save the name of the town in the set
    towns = towns | {splitted[0]} | {splitted[2]}

#Transform set into list
towns = list(towns)
#Make every possible permutation of the path
permutations = list(itertools.permutations(towns))

path_distance = dict()

#For each path
for path in permutations:

    total_distance = 0

    #Calculate total distance
    for index in range(len(path)-1):

        if (path[index]+"->"+path[index+1]) in distances:

            total_distance += distances[path[index]+"->"+path[index+1]]
        else:
            total_distance += distances[path[index+1]+"->"+path[index]]
    
    path_distance[path] = total_distance

#Sort paths by distance
path_distance = dict(sorted(path_distance.items(), key = lambda x: x[1]))

print("The shortest distance he can travel is",path_distance[list(path_distance.keys())[0]])



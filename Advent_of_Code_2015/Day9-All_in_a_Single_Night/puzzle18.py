# The next year, just to show off, Santa decides to take the route with the longest distance instead.

# He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

# For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

# What is the distance of the longest route?

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

print("The longest distance he can travel is",path_distance[list(path_distance.keys())[-1]])
# While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is 
# requesting as many containers as you can spare.

# Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number 
# of containers and still hold exactly 150 litres?

# In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

import itertools

#Read input
with open(r"Day17-No_Such_Thing_as_Too_Much\input.txt") as f:
    data = f.readlines()

#Volume of the eggnog
vol = 150
#List of containers
containers = []

#Save containers into the list
for container in data:
    containers.append(int(container.strip()))

#Combinations that can fit eggnog perfectly
combinations = []

#For each number of containers - 1 to all
for index in range(1,len(containers)+1):
    #Generate possible combinations with that many containers
    possible_combinations = itertools.combinations(containers,index)

    #For each combination check if it fits given volume perfectly
    for comb in possible_combinations:
        #If it does, save it to the list
        if sum(comb) == vol:
            combinations.append(comb)

#Sort valid combinations by number of containers
combinations = sorted(combinations, key = lambda x: len(x))
#Combinations that use only minimum number of containers
min_container_combinations = 0

#If the combination uses only minimum number of containers increase the counter
for comb in combinations:
    if len(comb) == len(combinations[0]):
        min_container_combinations += 1

print("You can fill the minimum number of containers in {} different ways".format(min_container_combinations))

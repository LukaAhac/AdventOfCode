# The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. 
# You take an inventory of the capacities of the available containers.

# For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

# 15 and 10
# 20 and 5 (the first 5)
# 20 and 5 (the second 5)
# 15, 5, and 5
# Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

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

print(len(combinations), "different combinations can fit 150L of eggnog perfectly")

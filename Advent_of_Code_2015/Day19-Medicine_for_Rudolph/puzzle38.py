# Now that the machine is calibrated, you're ready to begin molecule fabrication.

# Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time, just like the ones during calibration.

# For example, suppose you have the following replacements:

# e => H
# e => O
# H => HO
# H => OH
# O => HH
# If you'd like to make HOH, you start with e, and then make the following replacements:

# e => O to get O
# O => HH to get HH
# H => OH (on the second H) to get HOH
# So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be made in 6 steps.

# How long will it take to make the medicine? Given the available replacements and the medicine molecule in your puzzle input, 
# what is the fewest number of steps to go from e to the medicine molecule?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day19-Medicine_for_Rudolph\input.txt") as f:
    data = f.readlines()

#List of replacements
replacements = []

#Load all replacements, they are in input file up till last two rows
for line in data[:-2]:
    replacements.append(line.strip().split())

#Load starting molecule, located in last row of input file
starting_molecule = data[-1].strip()
#Iteration counter
iterations = 0

#while solution is not found
while True:

    #For each replacement going backwards
    for rep in replacements:

        #Calculate molecule lenght
        length = len(rep[-1])
        #Iterate over starting molecule up to the last - lenght + 1 index
        for index in range(len(starting_molecule)-length+1):
            #Check if you found molecule to replace
            if starting_molecule[index:index+length] == rep[-1]:
                #Replace molecule and set it for the next iteration
                starting_molecule = starting_molecule[:index] + rep[0] + starting_molecule[index+length:]
                #Increase counter
                iterations += 1
                #Go to next iteration
                break
    #Stop condition - "e" found
    if starting_molecule == "e":
        break

print(iterations,"is the fewest number of steps to go from e to the medicine molecule.")
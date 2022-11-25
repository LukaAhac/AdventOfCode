# Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

# Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine. 
# Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

# The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. 
# It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule.

# However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in 
# one step from a given starting point.

# For example, imagine a simpler machine that supports only the following replacements:

# H => HO
# H => OH
# O => HH
# Given the replacements above and starting with HOH, the following molecules could be generated:

# HOOH (via H => HO on the first H).
# HOHO (via H => HO on the second H).
# OHOH (via H => OH on the first H).
# HOOH (via H => OH on the second H).
# HHHH (via O => HH).
# So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement from HOH. Santa's favorite molecule, 
# HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and three from O).

# The machine replaces without regard for the surrounding characters. For example, given the string H2O, the transition H => OO would result in OO2O.

# Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine. 
# How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?

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
#Set that will hold distinct molecules
distinct_molecules = set()

#For each replacement
for rep in replacements:

    #Calculate molecule lenght
    length = len(rep[0])
    #Iterate over starting molecule up to the last - lenght + 1 index
    for index in range(len(starting_molecule)-length+1):
        #Check if you found molecule to replace
        if starting_molecule[index:index+length] == rep[0]:
            #Replace molecule and add it to the set
            distinct_molecules = distinct_molecules | {starting_molecule[:index] + rep[-1] + starting_molecule[index+length:]}

print(len(distinct_molecules),"distinct molecules can be created.")
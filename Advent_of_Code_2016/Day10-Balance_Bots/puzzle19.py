# You come upon a factory in which many robots are zooming around handing small microchips to each other.

# Upon closer examination, you notice that each bot only proceeds when it has two microchips, and once it does, 
# it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.

# Inspecting one of the microchips, it seems like they each contain a single number; the bots must use some logic to 
# decide what to do with each chip. You access the local control computer and download the bots' instructions (your puzzle input).

# Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the 
# instructions indicate what a given bot should do with its lower-value or higher-value chip.

# For example, consider the following instructions:

# value 5 goes to bot 2
# bot 2 gives low to bot 1 and high to bot 0
# value 3 goes to bot 1
# bot 1 gives low to output 1 and high to bot 0
# bot 0 gives low to output 2 and high to output 0
# value 2 goes to bot 2
# Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
# Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
# Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
# Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.
# In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip, and output bin 2 
# contains a value-3 microchip. In this configuration, bot number 2 is responsible for comparing value-5 microchips with
#  value-2 microchips.

# Based on your instructions, what is the number of the bot that is responsible for comparing value-61 microchips with 
# value-17 microchips?

#-----------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day10-Balance_Bots\input.txt") as f:
    data = f.readlines()

#Dictionary of bots
bots = dict()
#Dictionary of outputs
outputs = dict()

#For each bot instruction in data, create the bot with those instructions
for line in data:
    line = line.strip().split()
    
    if line[0] == "bot":
        #The bot has set that acts as hands for microships and dictionary with instrucions
        bots[line[1]] = [set(),{"low":[line[5],line[6]],"high":[line[10],line[11]]}]

#For each value instruction in data, add value to the correspoding bot
for line in data:
    line = line.strip().split()
    if line[0] == "value":
        bots[line[5]][0].add(int(line[1]))


#Until we find soultion
while True:

    #Iterate trought bots
    for key in bots.keys():

        botSpecs = bots[key]

        #If bot have 2 microchips
        if len(botSpecs[0]) == 2:

            #Check if we found the solution
            if 61 in botSpecs[0] and 17 in botSpecs[0]:
                print("The number of the bot that is responsible for comparing value-61 microchips with value-17 microchips is:",key)
                exit()

            #Else check if bot can give them to the others (If they dont already hold 2 microchips)
            else:
                if ((botSpecs[1]["low"][0] == "bot" and len(bots[botSpecs[1]["low"][1]][0]) < 2) \
                or botSpecs[1]["low"][0] == "output") and ((botSpecs[1]["high"][0] == "bot" \
                and len(bots[botSpecs[1]["high"][1]][0]) < 2) or botSpecs[1]["high"][0] == "output"):

                    #Lower and hiher value microchips
                    low,high = sorted(list(botSpecs[0]))

                    #Give the lower value microchip to the bot 
                    if botSpecs[1]["low"][0] == "bot":
                        bots[botSpecs[1]["low"][1]][0].add(low)
                    #Or but it into output basket
                    else:
                        if botSpecs[1]["low"][1] in outputs:
                            outputs[botSpecs[1]["low"][1]].add(low)
                        else:
                            outputs[botSpecs[1]["low"][1]]= {low}

                    #Give the higher value microchip to the bot 
                    if botSpecs[1]["high"][0] == "bot":
                        bots[botSpecs[1]["high"][1]][0].add(high)
                    #Or but it into output basket
                    else:
                        if botSpecs[1]["high"][1] in outputs:
                            outputs[botSpecs[1]["high"][1]].add(high)
                        else:
                            outputs[botSpecs[1]["high"][1]]= {high}

                    #Empty the set for bot that gave its microchips
                    bots[key][0] = set()

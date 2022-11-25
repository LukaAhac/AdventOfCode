# What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?

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

#Flag to note when we are done with the bot exchange
moreMicrochipsToProcess = True

#Until we find soultion
while moreMicrochipsToProcess:

    #Set the flag to false at the start of the loop
    moreMicrochipsToProcess = False

    #Iterate trought bots
    for key in bots.keys():

        botSpecs = bots[key]

        #If bot have 2 microchips
        if len(botSpecs[0]) == 2:

            #We have made the change and we need to check for another iteration
            moreMicrochipsToProcess = True

            #Check if bot can give them to the others (If they dont already hold 2 microchips)
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
                        outputs[botSpecs[1]["low"][1]].append(low)
                    else:
                        outputs[botSpecs[1]["low"][1]]= [low]

                 #Give the higher value microchip to the bot 
                if botSpecs[1]["high"][0] == "bot":
                    bots[botSpecs[1]["high"][1]][0].add(high)
                #Or but it into output basket
                else:
                    if botSpecs[1]["high"][1] in outputs:
                        outputs[botSpecs[1]["high"][1]].append(high)
                    else:
                        outputs[botSpecs[1]["high"][1]]= [high]

                #Empty the set for bot that gave its microchips
                bots[key][0] = set()


multipliedOutpus = outputs["0"][0]*outputs["1"][0]*outputs["2"][0]

print("If you multiply together the values of one chip in each of outputs 0, 1, and 2 you get:",multipliedOutpus)
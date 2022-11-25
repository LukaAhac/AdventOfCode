# As the submarine starts booting up things like the Retro Encabulator, 
# you realize that maybe you don't need all these submarine features after all.

# What is the smallest model number accepted by MONAD?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day24-Arithmetic_Logic_Unit\input.txt") as f:
    data = f.readlines()
    
#Given input
inp = []

#Parse input
for line in data:
    line = line.strip().split()
    inp.append(line)

#Dictionary of current states, where key is (z,w) and value is current number
#We are only tracking z and w value, since x and y reset to 0 each cycle
states = {(0,0):""}

#List of variables
variables = ["x","y","z","w"]
#Variable index dictionary
varIndex = {"x":0,"y":1,"z":2,"w":3}

instructionIndex = 0

#Go over each insttruction and applay it to all states
while instructionIndex < len(inp):

    #Read current instruction
    i = inp[instructionIndex]

    #States for next iteration
    newStates = dict()

    #If instruction is "inp" then expand every state with next digit (1..9)
    #If there is not that state (state is (z,w) tuple) in state dict then add it to the dict
    #If there is that state already in the dict, replace the old state only with SMALLER number
    if i[0] == "inp":

        for s in states:

            #Heuristics for accelerating progress
            #If this heuristic doestn work for you feel free to incerase it or compleatly remove it
            #The program will always work without heuristic but it would require some serious ram consumption (~6GB)
            #compared with (~1GB) when using 10**7 heuristic
            if s[0] >= 10**7:
                continue

            for digit in range(1,10):
                
                newS = list(s)
                newS[-1] = digit
                newS = tuple(newS)
                value = states[s] + str(digit)

                if newS not in newStates:
                    newStates[newS] = value
                elif newS in newStates and value < newStates[newS]:
                    newStates[newS] = value

        instructionIndex += 1
        states = newStates

    #When we are not dealing with "inp" instruction
    #Go over each state in the dict and performe 17 instructions that each cylce contains
    #After that swap the dicts for and go for next iteration
    else:

        for s in states:

            #Create temporary (x,y,z,w) state
            stat = [0,0,s[0],s[1]]

            for ind in range(instructionIndex,instructionIndex+17):

                i = inp[ind]

                if i[2] not in variables:
                        value2 = int(i[2])
                else:
                    value2 = stat[varIndex[i[2]]]

                if i[0] == "add":
                    stat[varIndex[i[1]]] += value2

                elif i[0] == "mul":
                    stat[varIndex[i[1]]] *= value2

                elif i[0] == "div":
                    stat[varIndex[i[1]]] //= value2


                elif i[0] == "mod":
                    stat[varIndex[i[1]]] %= value2

                elif i[0] == "eql":
                    if stat[varIndex[i[1]]] == value2:
                        stat[varIndex[i[1]]] = 1
                    else:
                        stat[varIndex[i[1]]] = 0

            newS = tuple(stat[2:])
            value = states[s]
            if newS not in newStates:
                newStates[newS] = value
            elif newS in newStates and value < newStates[newS]:
                newStates[newS] = value

        states = newStates
        instructionIndex += 17

#Get the biggest number found
validNumbers = []

for s in states:

    if s[0] == 0:
        validNumbers.append(states[s])

print("The smallest model number accepted by MONAD is :",max(validNumbers))
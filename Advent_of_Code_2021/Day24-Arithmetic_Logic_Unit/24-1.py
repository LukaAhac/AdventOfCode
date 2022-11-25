# Magic smoke starts leaking from the submarine's arithmetic logic unit (ALU). Without the ability to perform basic arithmetic 
# and logic functions, the submarine can't produce cool patterns with its Christmas lights!

# It also can't navigate. Or run the oxygen system.

# Don't worry, though - you probably have enough oxygen left to give you enough time to build a new ALU.

# The ALU is a four-dimensional processing unit: it has integer variables w, x, y, and z. These variables all start with the value 0. 
# The ALU also supports six instructions:

# inp a - Read an input value and write it to variable a.
# add a b - Add the value of a to the value of b, then store the result in variable a.
# mul a b - Multiply the value of a by the value of b, then store the result in variable a.
# div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. 
# (Here, "truncate" means to round the value toward zero.)
# mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
# eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.
# In all of these instructions, a and b are placeholders; a will always be the variable where the result of the operation is 
# stored (one of w, x, y, or z), while b can be either a variable or a number. Numbers can be positive or negative, but will always be integers.

# The ALU has no jump instructions; in an ALU program, every instruction is run exactly once in order from top to bottom. 
# The program halts after the last instruction has finished executing.

# (Program authors should be especially cautious; attempting to execute div with b=0 or attempting to execute mod with a<0 or 
# b<=0 will cause the program to crash and might even damage the ALU. These operations are never intended in any serious ALU program.)

# For example, here is an ALU program which takes an input number, negates it, and stores it in x:

# inp x
# mul x -1
# Here is an ALU program which takes two input numbers, then sets z to 1 if the second input number is three times larger than the 
# first input number, or sets z to 0 otherwise:

# inp z
# inp x
# mul z 3
# eql z x
# Here is an ALU program which takes a non-negative integer as input, converts it into binary, and stores the lowest (1's) bit in z, 
# the second-lowest (2's) bit in y, the third-lowest (4's) bit in x, and the fourth-lowest (8's) bit in w:

# inp w
# add z w
# mod z 2
# div w 2
# add y w
# mod y 2
# div w 2
# add x w
# mod x 2
# div w 2
# mod w 2
# Once you have built a replacement ALU, you can install it in the submarine, which will immediately resume what it was doing when 
# the ALU failed: validating the submarine's model number. To do this, the ALU will run the MOdel Number Automatic Detector program 
# (MONAD, your puzzle input).

# Submarine model numbers are always fourteen-digit numbers consisting only of digits 1 through 9. The digit 0 cannot appear 
# in a model number.

# When MONAD checks a hypothetical fourteen-digit model number, it uses fourteen separate inp instructions, each expecting a 
# single digit of the model number in order of most to least significant. (So, to check the model number 13579246899999, 
# you would give 1 to the first inp instruction, 3 to the second inp instruction, 5 to the third inp instruction, and so on.) 
# This means that when operating MONAD, each input instruction should only ever be given an integer value of at least 1 and at most 9.

# Then, after MONAD has finished running all of its instructions, it will indicate that the model number was valid by leaving 
# a 0 in variable z. However, if the model number was invalid, it will leave some other non-zero value in z.

# MONAD imposes additional, mysterious restrictions on model numbers, and legend says the last copy of the MONAD documentation was 
# eaten by a tanuki. You'll need to figure out what MONAD does some other way.

# To enable as many submarine features as possible, find the largest valid fourteen-digit model number that contains no 0 digits. 
# What is the largest model number accepted by MONAD?

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
    #If there is that state already in the dict, replace the old state only with BIGGER number
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
                elif newS in newStates and value > newStates[newS]:
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
            elif newS in newStates and value > newStates[newS]:
                newStates[newS] = value

        states = newStates
        instructionIndex += 17

#Get the biggest number found
validNumbers = []

for s in states:

    if s[0] == 0:
        validNumbers.append(states[s])

print("The largest model number accepted by MONAD is :",max(validNumbers))
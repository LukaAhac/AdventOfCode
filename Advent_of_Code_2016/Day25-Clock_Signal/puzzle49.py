# You open the door and find yourself on the roof. The city sprawls away from you for miles and miles.

# There's not much time now - it's already Christmas, but you're nowhere near the North Pole, much too 
# far to deliver these stars to the sleigh in time.

# However, maybe the huge antenna up here can offer a solution. After all, the sleigh doesn't need the stars, 
# exactly; it needs the timing data they provide, and you happen to have a massive signal generator right here.

# You connect the stars you have to your prototype computer, connect that to the antenna, and begin the transmission.

# Nothing happens.

# You call the service number printed on the side of the antenna and quickly explain the situation. 
# "I'm not sure what kind of equipment you have connected over there," he says, "but you need a clock signal." 
# You try to explain that this is a signal for a clock.

# "No, no, a clock signal - timing information so the antenna computer knows how to read the data you're sending it. 
# An endless, alternating pattern of 0, 1, 0, 1, 0, 1, 0, 1, 0, 1...." He trails off.

# You ask if the antenna can handle a clock signal at the frequency you would need to use for the data from the stars. 
# "There's no way it can! The only antenna we've installed capable of that is on top of a top-secret Easter 
# Bunny installation, and you're definitely not-" You hang up the phone.

# You've extracted the antenna's clock signal generation assembunny code (your puzzle input); it looks mostly 
# compatible with code you worked on just recently.

# This antenna code, being a signal generator, uses one extra instruction:

# out x transmits x (either an integer or the value of a register) as the next value for the clock signal.
# The code takes a value (via register a) that describes the signal to generate, but you're not sure how it's used. 
# You'll have to find the input to produce the right signal through experimentation.

# What is the lowest positive integer that can be used to initialize register a and cause the code to output 
# a clock signal of 0, 1, 0, 1... repeating forever?

#-----------------------------------------------------------------------------------------------------------


#Read input
with open(r"Day25-Clock_Signal\input.txt") as f:
    data = f.readlines()

#Instruction list
assembunnyCode = []

#Prepare instructions
for instruction in data:
    instruction = instruction.strip().split()
    assembunnyCode.append(instruction)

#Function to check if the string consist of alternating 0s and 1s starting with 0
#Returns True if it does, False otherwise
def checkStr(string):

    for index in range(len(string)):

        if index%2 == 0:
            if string[index] != "0":
                return False
        else:
            if string[index] != "1":
                return False

    return True


#Number we are trying to find, we try with value = 0
lowestInteger = -1

#Until we find lowest integer
while True:

    #Increase it for next iteration
    lowestInteger += 1

    #Reset the registers, and output
    register = {"a" : lowestInteger, "b" : 0, "c" : 0, "d" : 0}
    outString = ""

    #Instruction index
    index = 0

    #While we dont form the output of lenght 10, the lenght of 10 is here choosen arbitrary
    #We can always use higher lenght to compare with but it will increase the runtime of the programm
    #We can even use some smalelr lenght like 7 and it will still work for my input, but the higher we pick
    #more sure we are that the answer is correct
    while len(outString)<=10:

        #Fetch the current instruction
        currentInstruction = assembunnyCode[index]

        #If it is cpy see wheter we need to copy a number or from a register to another register
        if currentInstruction[0] == "cpy":

            if currentInstruction[1] not in {"a","b","c","d"}:

                register[currentInstruction[2]] = int(currentInstruction[1])

            else:

                register[currentInstruction[2]] = register[currentInstruction[1]]

        #If it is inc, just increment given register
        elif currentInstruction[0] == "inc":

            register[currentInstruction[1]] += 1

        #If it is dec, just decrement given register
        elif currentInstruction[0] == "dec":

            register[currentInstruction[1]] -= 1

        #If it is jnz, fetch the condition number(either from a register or directly from instruction)
        #If condition is not zero, jump (change index) for given amount
        elif currentInstruction[0] == "jnz":

            if currentInstruction[1] not in {"a","b","c","d"}:

                condition = int(currentInstruction[1])

            else:

                condition = register[currentInstruction[1]]

            if currentInstruction[2] not in {"a","b","c","d"}:
                jumping = int(currentInstruction[2])
            else:
                jumping = register[currentInstruction[2]]

            if condition != 0:

                index += jumping
                continue

        #If instruction is "out" then append the value (given or in register) to the outString
        elif currentInstruction[0] == "out":

            if currentInstruction[1] not in {"a","b","c","d"}:

                outString = outString + str(currentInstruction[1])
            else:

                outString = outString + str(register[currentInstruction[1]])

        #Go to the next instruction
        index += 1

    #If we found the string that consists of alternating 0s and 1s starting with 0, we are done
    if checkStr(outString):
        print("The lowest positive integer that can be used to initialize register a and cause the code to output a clock signal of 0, 1, 0, 1... repeating forever is:",\
            lowestInteger)
        quit()
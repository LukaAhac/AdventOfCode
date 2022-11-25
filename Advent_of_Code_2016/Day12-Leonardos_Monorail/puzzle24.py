# As you head down the fire escape to the monorail, you notice it didn't start; register c
# needs to be initialized to the position of the ignition key.

# If you instead initialize register c to be 1, what value is now left in register a?

#-----------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day12-Leonardos_Monorail\input.txt") as f:
    data = f.readlines()


#Register dictionary
register = {"a" : 0, "b" : 0, "c" : 1, "d" : 0}
#Instruction list
assembunnyCode = []

#Prepare instructions
for instruction in data:
    instruction = instruction.strip().split()
    assembunnyCode.append(instruction)

#Instruction index
index = 0

#While we dont reach end
while index < len(assembunnyCode):

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

        if condition != 0:

            index += int(currentInstruction[2])
            continue

    #Go to the next instruction
    index += 1


print("Value left in register a is:",register["a"])
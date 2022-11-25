# The safe doesn't open, but it does make several angry noises to express its frustration.

# You're quite sure your logic is working correctly, so the only other thing is... you check 
# the painting again. As it turns out, colored eggs are still eggs. Now you count 12.

# As you run the program with this new input, the prototype computer begins to overheat. 
# You wonder what's taking so long, and whether the lack of any instruction more powerful 
# than "add one" has anything to do with it. Don't bunnies usually multiply?

# Anyway, what value should actually be sent to the safe?

#-----------------------------------------------------------------------------------------------------------

#NOTE: Assembuny code for this part was modified with new "mul" instruciton that performs multiplciation
#Upon closer inspection we can see that lines 5-10 are performing multiplication of register b and d while
#storing result into register a, assembuny code was modified to use "mul" instruction insted and the code
#was appended with "mul" instruction. We can replace those slow multiplication through addition with fast
#mul instruction because uppon closer inspection we can see that toggle never targets any of thouse instrucitons
#that we replace and we wont gent in trouble with repalcing them, but there is one more thing we need to take care
#of and that is "cpy -16 c" which is in the line 18 of the original assembuny code, That instructions copies value -16
#to the register c which then always jumps that amount (Those two instrcutions always jump code to the 2nd line),since
#we removed 5 lines of assembuny code we also need to jump 5 places less so we replace value -16 with value -15

#Read input
with open(r"Day23-Safe_Cracking\input2.txt") as f:
    data = f.readlines()

#Register dictionary
register = {"a" : 12, "b" : 0, "c" : 0, "d" : 0}
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
    #print(currentInstruction)

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
    
    #If instruction is tgl, we toggle the instruction according to rules given in task
    elif currentInstruction[0] == "tgl":

        if currentInstruction[1] not in {"a","b","c","d"}:
            toggleIndex = index + int(currentInstruction[1])
        else:
            toggleIndex = index + register[currentInstruction[1]]

        if toggleIndex < len(assembunnyCode):
            instructionToToggle = assembunnyCode[toggleIndex][0]

            if instructionToToggle == "inc":
                toggleTo = "dec"
            elif instructionToToggle in {"dec","tgl"}:
                toggleTo = "inc"
            elif instructionToToggle == "jnz":
                toggleTo = "cpy"
            elif instructionToToggle == "cpy":
                toggleTo = "jnz"

            assembunnyCode[toggleIndex][0] = toggleTo

    #NOTE: This instruction (like suggested in the task) was added by me
    #And assembuny code was modified to use multiplication
    elif currentInstruction[0] == "mul":

        register[currentInstruction[3]] += register[currentInstruction[2]] * register[currentInstruction[1]]
 
    #Go to the next instruction
    index += 1


print("The value that should be actually sent to the safe is :",register["a"])
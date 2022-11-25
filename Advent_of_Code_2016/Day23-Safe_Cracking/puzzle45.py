# This is one of the top floors of the nicest tower in EBHQ. The Easter Bunny's private office is here, complete with 
# a safe hidden behind a painting, and who wouldn't hide a star in a safe behind a painting?

# The safe has a digital screen and keypad for code entry. A sticky note attached to the safe has a password hint on 
# it: "eggs". The painting is of a large rabbit coloring some eggs. You see 7.

# When you go to type the code, though, nothing appears on the display; instead, the keypad comes 
# apart in your hands, apparently having been smashed. Behind it is some kind of socket - one that matches 
# a connector in your prototype computer! You pull apart the smashed keypad and extract the logic circuit, 
# plug it into your computer, and plug your computer into the safe.

# Now, you just need to figure out what output the keypad would have sent to the safe. You extract the assembunny 
# code from the logic chip (your puzzle input).
# The code looks like it uses almost the same architecture and instruction set that the monorail computer used! 
# You should be able to use the same assembunny interpreter for this as you did there, but with one new instruction:

# tgl x toggles the instruction x away (pointing at instructions like jnz does: positive means forward; 
# negative means backward):

# For one-argument instructions, inc becomes dec, and all other one-argument instructions become inc.
# For two-argument instructions, jnz becomes cpy, and all other two-instructions become jnz.
# The arguments of a toggled instruction are not affected.
# If an attempt is made to toggle an instruction outside the program, nothing happens.
# If toggling produces an invalid instruction (like cpy 1 2) and an attempt is later made to execute that 
# instruction, skip it instead.
# If tgl toggles itself (for example, if a is 0, tgl a would target itself and become inc a), the resulting 
# instruction is not executed until the next time it is reached.
# For example, given this program:

# cpy 2 a
# tgl a
# tgl a
# tgl a
# cpy 1 a
# dec a
# dec a
# cpy 2 a initializes register a to 2.
# The first tgl a toggles an instruction a (2) away from it, which changes the third tgl a into inc a.
# The second tgl a also modifies an instruction 2 away from it, which changes the cpy 1 a into jnz 1 a.
# The fourth line, which is now inc a, increments a to 3.
# Finally, the fifth line, which is now jnz 1 a, jumps a (3) instructions ahead, skipping the dec a instructions.
# In this example, the final value in register a is 3.

# The rest of the electronics seem to place the keypad entry (the number of eggs, 7) in register a, run the code, 
# and then send the value left in register a to the safe.

# What value should be sent to the safe?

#-----------------------------------------------------------------------------------------------------------

#NOTE: This is code taken from Day 12 and only appended with instruction "tgl x"

#Read input
with open(r"Day23-Safe_Cracking\input.txt") as f:
    data = f.readlines()

#Register dictionary
register = {"a" : 7, "b" : 0, "c" : 0, "d" : 0}
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

    #Go to the next instruction
    index += 1


print("The value that should be sent to the safe is :",register["a"])
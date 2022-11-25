# You finally reach the top floor of this building: a garden with a slanted glass ceiling. 
# Looks like there are no more stars to be had.

# While sitting on a nearby bench amidst some tiger lilies, you manage to decrypt some of the files you 
# extracted from the servers downstairs.

# According to these documents, Easter Bunny HQ isn't just this building - it's a collection of buildings 
# in the nearby area. They're all connected by a local monorail, and there's another building not far from 
# here! Unfortunately, being night, the monorail is currently not operating.

# You remotely connect to the monorail control systems and discover that the boot sequence expects a password. 
# The password-checking logic (your puzzle input) is easy to extract, but the code it uses is strange: 
# it's assembunny code designed for the new computer you just assembled. You'll have to execute the code
#  and get the password.

# The assembunny code you've extracted operates on four registers (a, b, c, and d) that start at 0 and 
# can hold any integer. However, it seems to make use of only a few instructions:

# cpy x y copies x (either an integer or the value of a register) into register y.
# inc x increases the value of register x by one.
# dec x decreases the value of register x by one.
# jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x 
# is not zero.
# The jnz instruction moves relative to itself: an offset of -1 would continue at the previous instruction,
#  while an offset of 2 would skip over the next instruction.

# For example:

# cpy 41 a
# inc a
# inc a
# dec a
# jnz a 2
# dec a
# The above code would set register a to 41, increase its value by 2, decrease its value by 1, and then skip 
# the last dec a (because a is not zero, so the jnz a 2 skips it), leaving register a at 42. When you move past 
# the last instruction, the program halts.

# After executing the assembunny code in your puzzle input, what value is left in register a?

#-----------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day12-Leonardos_Monorail\input.txt") as f:
    data = f.readlines()

#Register dictionary
register = {"a" : 0, "b" : 0, "c" : 0, "d" : 0}
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
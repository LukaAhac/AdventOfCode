# Little Jane Marie just got her very first computer for Christmas from some unknown benefactor. 
# It comes with instructions and an example program, but the computer itself seems to be malfunctioning. 
# She's curious what the program does, and would like you to help her run it.

# The manual explains that the computer supports two registers and six instructions (truly, it goes on to remind the reader, a state-of-the-art technology). 
# The registers are named a and b, can hold any non-negative integer, and begin with a value of 0. The instructions are as follows:

# hlf r sets register r to half its current value, then continues with the next instruction.
# tpl r sets register r to triple its current value, then continues with the next instruction.
# inc r increments register r, adding 1 to it, then continues with the next instruction.
# jmp offset is a jump; it continues with the instruction offset away relative to itself.
# jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
# jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
# All three jump instructions work with an offset relative to that instruction. 
# The offset is always written with a prefix + or - to indicate the direction of the jump (forward or backward, respectively). 
# For example, jmp +1 would simply continue with the next instruction, while jmp +0 would continuously jump back to itself forever.

# The program exits when it tries to run an instruction beyond the ones defined.

# For example, this program sets a to 2, because the jio instruction causes it to skip the tpl instruction:

# inc a
# jio a, +2
# tpl a
# inc a
# What is the value in register b when the program in your puzzle input is finished executing?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day23-Opening_the_Turing_Lock\input.txt") as f:
    data = f.readlines()


#Registers
a = 0
b = 0
#List of instructions
instruction_list = []

#Load instructions into list
for line in data:
    instruction_list.append(line.strip().split())

#Variable that tracks position of an instruction
position = 0


while True:

    #If we went beyond last instruction, exit the program
    if position >= len(instruction_list):
        break
    
    #Load instruction
    instruction = instruction_list[position]

    #If instruction is "hlf", halve the required register and increment position
    if instruction[0] == "hlf":
        if instruction[1] == "a":
            a /= 2
        else:
            b /= 2
        position += 1
    #If instruction is "tpl", triple the required register and increment position
    elif instruction[0] == "tpl":
        if instruction[1] == "a":
            a *= 3
        else:
            b *= 3
        position += 1
    #If instruction is "inc", increment the required register and increment position
    elif instruction[0] == "inc":
        if instruction[1] == "a":
            a += 1
        else:
            b += 1
        position += 1
    #If instruction is "jmp", increase position for required amount
    elif instruction[0] == "jmp":
        position += int(instruction[1])
    #If instruction is "jie", load the required register, check if is is even and increase position for rquired amount if it is, if it is not increment position
    elif instruction[0] == "jie":
        if instruction[1][0] == "a":
            reg = a
        else:
            reg = b

        if reg % 2 == 0:
            position += int(instruction[2])
        else:
            position += 1
    #If instruction is "jio", load the required register, check if is is one and increase position for rquired amount if it is, if it is not increment position
    elif instruction[0] == "jio":
        if instruction[1][0] == "a":
            reg = a
        else:
            reg = b

        if reg == 1:
            position += int(instruction[2])
        else:
            position += 1

print("At the end of the program, value in register b is:",b)
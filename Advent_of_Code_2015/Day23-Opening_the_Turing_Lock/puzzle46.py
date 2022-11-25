# The unknown benefactor is very thankful for releasi-- er, helping little Jane Marie with her computer. 
# Definitely not to distract you, what is the value in register b after the program is finished executing if register a starts as 1 instead?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day23-Opening_the_Turing_Lock\input.txt") as f:
    data = f.readlines()


#Registers
a = 1
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
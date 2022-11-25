# Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). 
# What new signal is ultimately provided to wire a?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day7-Some_Assembly_Required\input.txt") as f:
    data = f.readlines()

#Override the wire b with the new signal
for index in range(len(data)):
    if (data[index].strip().split())[-1] == "b":
        data[index] = "956 -> b"

solved_wires = dict()
changesDone = True

#Loop until all wires are solved
while changesDone:

    #Set flag to False
    changesDone = False

    #For instruction in data
    for instruction in data:

        splitted = instruction.strip().split()

        #If the wire is already solved skip to the next wire
        if splitted[-1] in solved_wires:
            continue
        
        #If it is one of binary operations
        if "OR" in splitted or "AND" in splitted or "LSHIFT" in splitted or "RSHIFT" in splitted:
            #Check if the first variable is a number
            if splitted[0].isnumeric():
                first = int(splitted[0])
            #If it is not a number check if the wire is solved already
            elif splitted[0] in solved_wires:
                first = solved_wires[splitted[0]]
            #If it is not a number and it is not solved skip to next instruction
            else:
                continue
            #Check if the second variable is a number
            if splitted[2].isnumeric():
                second = int(splitted[2])
            #If it is not a number check if the wire is solved already
            elif splitted[2] in solved_wires:
                second = solved_wires[splitted[2]]
            #If it is not a number and it is not solved skip to next instruction
            else:
                continue
            #Both variables are number os solved wires so changes will be made
            changesDone = True
            #If it is OR operation, solve new wire by performing bitwise OR
            if splitted[1] == "OR":
                solved_wires[splitted[-1]] = first | second
            #If it is AND operation, solve new wire by performing bitwise AND
            elif splitted[1] == "AND":
                solved_wires[splitted[-1]] = first & second
            #If it is LSHIFT operation, solve new wire by performing bitwise LSHIFT
            elif splitted[1] == "LSHIFT":
                solved_wires[splitted[-1]] = first << second
            #If it is RSHIFT operation, solve new wire by performing bitwise RSHIFT
            elif splitted[1] == "RSHIFT":
                solved_wires[splitted[-1]] = first >> second
        #If it is not binary operation check if it is unary NOT operation
        elif "NOT" in splitted:
            #Check if the first variable is a number
            if splitted[1].isnumeric():
                first = int(splitted[1])
            #If it is not a number check if the wire is solved already
            elif splitted[1] in solved_wires:
                first = solved_wires[splitted[1]]
            #If it is not a number and it is not solved skip to next instruction
            else:
                continue
            #Variable is number os solved wires so changes will be made
            changesDone = True
            #Solve new wire by performing bitwse NOT
            solved_wires[splitted[-1]] = ~first
        else:
            #Check if the first variable is a number
            if splitted[0].isnumeric():
                first = int(splitted[0])
            #If it is not a number check if the wire is solved already
            elif splitted[0] in solved_wires:
                first = solved_wires[splitted[0]]
            #If it is not a number and it is not solved skip to next instruction
            else:
                continue
            #Variable is number os solved wires so changes will be made
            changesDone = True
            #Brdige variable to the new wire
            solved_wires[splitted[-1]] = first

print("The signal provided to the wire a is",solved_wires["a"])
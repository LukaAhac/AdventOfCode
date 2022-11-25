# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range,
# and he needs help assembling the circuit.

# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, 
# another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. 
# A gate provides no signal until all of its inputs have a signal.

# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, 
# and then connect its output to wire z.
# For example:

# 123 -> x means that the signal 123 is provided to wire x.
# x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
# p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
# NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, 
# almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

# For example, here is a simple circuit:

# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# After it is run, these are the signals on the wires:

# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456
# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day7-Some_Assembly_Required\input.txt") as f:
    data = f.readlines()

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
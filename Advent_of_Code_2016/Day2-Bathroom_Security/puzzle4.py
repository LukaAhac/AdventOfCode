# You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many 
# fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, 
# the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours 
# of bathroom-keypad-design meetings:

#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D
# You still start at "5" and stop when you're at an edge, but given the same instructions as above, 
# the outcome is very different:

# You start at "5" and don't move at all (up and left are both edges), ending at 5.
# Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), 
# ending at D.
# Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
# Finally, after five more moves, you end at 3.
# So, given the actual keypad layout, the code would be 5DB3.

# Using the same instructions in your puzzle input, what is the correct bathroom code?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day2-Bathroom_Security\input.txt") as f:
    data = f.readlines()

#List of instructions
instructions = []

for line in data:
    instructions.append(line.strip())

#Weird key pad
key_pad = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,"A","B","C",0],[0,0,"D",0,0]]

#Starting numver is 5, which is on x=0, y=2
starting_coords = [0,2]

#Bathroom code
code = []


#For each instruction do the moves
for instruction in instructions:

    moves = list(instruction)

    #For each move
    for move in moves:

        #If the move is L go 1 place left if current number is not the left-most keys
        if move == "L" and starting_coords[0] != 0:

            starting_coords[0] -= 1

            #If the move puts us out of the weird key pad, move back
            if key_pad[starting_coords[1]][starting_coords[0]] == 0:
                starting_coords[0] += 1

        #If the move is R go 1 place right if the current number is not the right-most keys
        elif move == "R" and starting_coords[0] != 4:

            starting_coords[0] += 1

            #If the move puts us out of the weird key pad, move back
            if key_pad[starting_coords[1]][starting_coords[0]] == 0:
                starting_coords[0] -= 1

        #If the move is U go one place up if the curent number is not the upper keys
        elif move == "U" and starting_coords[1] != 0:

            starting_coords[1] -= 1

            #If the move puts us out of the weird key pad, move back
            if key_pad[starting_coords[1]][starting_coords[0]] == 0:
                starting_coords[1] += 1

        #If the move is D go one place down if the current number is not the lower keys
        elif move == "D" and starting_coords[1] != 4:

            starting_coords[1] += 1

            #If the move puts us out of the weird key pad, move back
            if key_pad[starting_coords[1]][starting_coords[0]] == 0:
                starting_coords[1] -= 1

    code.append(key_pad[starting_coords[1]][starting_coords[0]])

#Convert code to string - for printing
code = list(map(str,code))

print("The code for the bathroom is:","".join(code))
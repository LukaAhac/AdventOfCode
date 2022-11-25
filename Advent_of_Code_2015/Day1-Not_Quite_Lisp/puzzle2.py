# Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). 
# The first character in the instructions has position 1, the second character has position 2, and so on.

# For example:

# ) causes him to enter the basement at character position 1.
# ()()) causes him to enter the basement at character position 5.
# What is the position of the character that causes Santa to first enter the basement?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day1-Not_Quite_Lisp\input.txt") as f:
    data = f.readlines()

#Input is only one row
data = data[0]

left_brackets = 0
right_brackets = 0

#Count the number of brackets
for position in range(len(data)):
    if data[position] == "(":
        left_brackets += 1
    else:
        right_brackets += 1
    
    #Check if the differecne between left brackets and right brackets is -1 (basement)
    if (left_brackets - right_brackets) == -1:
        print("Position of the character is:",(position+1))
        break

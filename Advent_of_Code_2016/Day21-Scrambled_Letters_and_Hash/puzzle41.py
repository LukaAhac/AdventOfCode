# The computer system you're breaking into uses a weird scrambling function to store its passwords. 
# It shouldn't be much trouble to create your own scrambled password so you can add it to the system; 
# you just have to implement the scrambler.

# The scrambling function is a series of operations (the exact list is provided in your puzzle input).
# Starting with the password to be scrambled, apply each operation in succession to the string. 
# The individual operations behave as follows:

# swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.
# swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where 
# they appear in the string).
# rotate left/right X steps means that the whole string should be rotated; for example, one right rotation 
# would turn abcd into dabc.
# rotate based on position of letter X means that the whole string should be rotated to the right based on 
# the index of letter X (counting from 0) as determined before this instruction does any rotations. 
# Once the index is determined, rotate the string to the right one time, plus a number of times equal 
# to that index, plus one additional time if the index was at least 4.
# reverse positions X through Y means that the span of letters at indexes X through Y (including the 
# letters at X and Y) should be reversed in order.
# move position X to position Y means that the letter which is at index X should be removed from the string, 
# then inserted such that it ends up at index Y.
# For example, suppose you start with abcde and perform the following operations:

# swap position 4 with position 0 swaps the first and last letters, producing the input 
# for the next step, ebcda.
# swap letter d with letter b swaps the positions of d and b: edcba.
# reverse positions 0 through 4 causes the entire string to be reversed, producing abcde.
# rotate left 1 step shifts all letters left one position, causing the first letter to wrap to the end of 
# the string: bcdea.
# move position 1 to position 4 removes the letter at position 1 (c), then inserts it at position 4 
# (the end of the string): bdeac.
# move position 3 to position 0 removes the letter at position 3 (a), then inserts it at position 0 
# (the front of the string): abdec.
# rotate based on position of letter b finds the index of letter b (1), then rotates the string right once 
# plus a number of times equal to that index (2): ecabd.
# rotate based on position of letter d finds the index of letter d (4), then rotates the string right once, 
# plus a number of times equal to that index, plus an additional time because the index was at least 4, 
# for a total of 6 right rotations: decab.
# After these steps, the resulting scrambled password is decab.

# Now, you just need to generate a new scrambled password and you can access the system. Given the list of 
# scrambling operations in your puzzle input, what is the result of scrambling abcdefgh?

#-----------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day21-Scrambled_Letters_and_Hash\input.txt") as f:
    data = f.readlines()

#List of scrambling instructions
instructions = []

#Fetch the instructions
for line in data:
    instructions.append(line.strip().split())

#Given password that we need to scramble
passwordToScramble = "abcdefgh"

#Perform each instruction
for instruction in instructions:

    #If insttructions is swap
    if instruction[0] == "swap":

        #Turn the string into the list for easier swaping
        listOfLetters = list(passwordToScramble)

        #If instruction is swap positions then swap by positions
        if instruction[1] == "position":

            temp = listOfLetters[int(instruction[2])]
            listOfLetters[int(instruction[2])] = listOfLetters[int(instruction[5])]
            listOfLetters[int(instruction[5])] = temp
        
        #If instruction is swap letters, then swap that letters
        elif instruction[1] == "letter":

            position1 = passwordToScramble.index(instruction[2])
            position2 = passwordToScramble.index(instruction[5])

            temp = listOfLetters[position1]
            listOfLetters[position1] = listOfLetters[position2]
            listOfLetters[position2] = temp

        #Join the list back to the string
        passwordToScramble = "".join(listOfLetters)
    
    #If the instruction is rotate
    elif instruction[0] == "rotate":

        #If the instruction is rotate left, then rotet left
        if instruction[1] == "left":

            steps = int(instruction[2])

            if steps > len(passwordToScramble):
                steps = steps % len(passwordToScramble)

            passwordToScramble = passwordToScramble[steps:] + passwordToScramble[:steps]

        #If the instrution is rotate right, then rotate right
        elif instruction[1] == "right":

            steps = int(instruction[2])

            if steps > len(passwordToScramble):
                steps = steps % len(passwordToScramble)

            passwordToScramble = passwordToScramble[-steps:] + passwordToScramble[:-steps]

        #If the instruction is rotate based on the position of a letter, then calcualte rotations and rotate right
        elif instruction[1] == "based":

            steps = passwordToScramble.index(instruction[6])
            if steps >= 4:
                steps += 2
            else:
                steps += 1

            if steps > len(passwordToScramble):
                steps = steps % len(passwordToScramble)

            passwordToScramble = passwordToScramble[-steps:] + passwordToScramble[:-steps]
    
    #If instruction is reverse, then reverse the given substring
    elif instruction[0] == "reverse":

        position1 = int(instruction[2])
        position2 = int(instruction[4])

        toReverse = passwordToScramble[position1:position2+1]

        passwordToScramble = passwordToScramble[:position1] + toReverse[::-1] \
        + passwordToScramble[position2+1:]

    #If instruction is move, then remove the letter and put it to the desired position
    elif instruction[0] == "move":

        removeIndex = int(instruction[2])
        putIndex = int(instruction[5])
        char = passwordToScramble[removeIndex]

        passwordToScramble = passwordToScramble[:removeIndex] + passwordToScramble[removeIndex+1:]
        passwordToScramble = passwordToScramble[:putIndex] + char + passwordToScramble[putIndex:]

print("The result of scrambling abcdefgh is:",passwordToScramble)
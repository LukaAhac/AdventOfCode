# You scrambled the password correctly, but you discover that you can't actually modify the password 
# file on the system. You'll need to un-scramble one of the existing passwords by reversing the scrambling process.

# What is the un-scrambled version of the scrambled password fbgdceah?

#-----------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day21-Scrambled_Letters_and_Hash\input.txt") as f:
    data = f.readlines()

#List of scrambling instructions
instructions = []

#Fetch the instructions
for line in data:
    instructions.append(line.strip().split())

#Reverse the list of the instructions
instructions = instructions[::-1]

#Given password that we need to unscramble
passwordToScramble = "fbgdceah"

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

        #If the instruction is rotate left, then rotet right!!!!!
        if instruction[1] == "left":

            steps = int(instruction[2])

            if steps > len(passwordToScramble):
                steps = steps % len(passwordToScramble)

            passwordToScramble = passwordToScramble[-steps:] + passwordToScramble[:-steps]

        #If the instrution is rotate right, then rotate left!!!!
        elif instruction[1] == "right":

            steps = int(instruction[2])

            if steps > len(passwordToScramble):
                steps = steps % len(passwordToScramble)

            passwordToScramble = passwordToScramble[steps:] + passwordToScramble[:steps]

        #If the instruction is rotate based on the position of a letter, finde the reverse by bruteforcing
        elif instruction[1] == "based":

            allRotations = []
            #Make a list of all possible rotations and check wheter of that gives the output that we need to reverse
            for index in range(len(passwordToScramble)):

                allRotations.append(passwordToScramble[index:] + passwordToScramble[:index])

            for rotation in allRotations:

                steps = rotation.index(instruction[6])
                if steps >= 4:
                    steps += 2
                else:
                    steps += 1

                if steps > len(rotation):
                    steps = steps % len(rotation)

                rotationDone = rotation[-steps:] + rotation[:-steps]

                if rotationDone == passwordToScramble:

                    passwordToScramble = rotation
                    break
    
    #If instruction is reverse, then reverse the given substring
    elif instruction[0] == "reverse":

        position1 = int(instruction[2])
        position2 = int(instruction[4])

        toReverse = passwordToScramble[position1:position2+1]

        passwordToScramble = passwordToScramble[:position1] + toReverse[::-1] \
        + passwordToScramble[position2+1:]

    #If instruction is move, then remove the letter and put it to the desired position,
    #but revetrse the indexes
    elif instruction[0] == "move":

        removeIndex = int(instruction[5])
        putIndex = int(instruction[2])
        char = passwordToScramble[removeIndex]

        passwordToScramble = passwordToScramble[:removeIndex] + passwordToScramble[removeIndex+1:]
        passwordToScramble = passwordToScramble[:putIndex] + char + passwordToScramble[putIndex:]

print("The un-scrambled version of the scrambled password fbgdceah is:",passwordToScramble)
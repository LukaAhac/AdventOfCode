# The Elves contact you over a highly secure emergency channel. Back at the North Pole, 
# the Elves are busy misunderstanding White Elephant parties.

# Each Elf brings a present. They all sit in a circle, numbered starting with position 1. 
# Then, starting with the first Elf, they take turns stealing all the presents from the Elf to their left. 
# An Elf with no presents is removed from the circle and does not take turns.

# For example, with five Elves (numbered 1 to 5):

#   1
# 5   2
#  4 3
# Elf 1 takes Elf 2's present.
# Elf 2 has no presents and is skipped.
# Elf 3 takes Elf 4's present.
# Elf 4 has no presents and is also skipped.
# Elf 5 takes Elf 1's two presents.
# Neither Elf 1 nor Elf 2 have any presents, so both are skipped.
# Elf 3 takes Elf 5's three presents.
# So, with five Elves, the Elf that sits starting in position 3 gets all the presents.

# With the number of Elves given in your puzzle input, which Elf gets all the presents?

# Your puzzle input is 3012210.

#-----------------------------------------------------------------------------------------------------------

#Given number of elves
numberOfElves = 3012210

#Make the list of elves
elves = [1]*numberOfElves

#Index of the elf that is taking the presents
takingIndex = None

#Until the game is not finished
while True:

    #Iterate throught elves
    for index in range(len(elves)):

        #If elf has no presents, he is out of the game
        if elves[index] == 0:
            continue
        #If elf has presents and its his turn to take the gift, mark his index
        elif takingIndex is None:
            takingIndex = index
        #Take the gift from the current elf and give them to the elf that is supposed to take them
        else:
            elves[takingIndex] += elves[index]
            #If the elf that got gifts have them all now, game is over
            if elves[takingIndex] == numberOfElves:
                print("Elf {} gets all the presents".format(takingIndex+1))
                quit()
            elves[index] = 0
            takingIndex = None
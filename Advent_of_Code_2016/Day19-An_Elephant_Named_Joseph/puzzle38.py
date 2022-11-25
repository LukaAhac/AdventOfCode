# Realizing the folly of their present-exchange rules, the Elves agree to instead steal presents 
# from the Elf directly across the circle. If two Elves are across the circle, the one on the left 
# (from the perspective of the stealer) is stolen from. The other rules remain unchanged: Elves with no 
# presents are removed from the circle entirely, and the other elves move in slightly to keep the circle 
# evenly spaced.

# For example, with five Elves (again numbered 1 to 5):

# The Elves sit in a circle; Elf 1 goes first:
#   1
# 5   2
#  4 3
# Elves 3 and 4 are across the circle; Elf 3's present is stolen, being the one to the left. Elf 3 leaves 
# the circle, and the rest of the Elves move in:
#   1           1
# 5   2  -->  5   2
#  4 -          4
# Elf 2 steals from the Elf directly across the circle, Elf 5:
#   1         1 
# -   2  -->     2
#   4         4 
# Next is Elf 4 who, choosing between Elves 1 and 2, steals from Elf 1:
#  -          2  
#     2  -->
#  4          4
# Finally, Elf 2 steals from Elf 4:
#  2
#     -->  2  
#  -
# So, with five Elves, the Elf that sits starting in position 2 gets all the presents.

# With the number of Elves given in your puzzle input, which Elf now gets all the presents?

#-----------------------------------------------------------------------------------------------------------
import math

#Given number of elves
numberOfElves = 3012210

#Make the list of elves
elves = []
for elf in range(numberOfElves):
    elves.append([elf+1,1])

#Current index in the list we are working on
currentIndex = 0

#Until we are left with only one elf
while len(elves) > 1:

    #If the current index is the last index in the lest, then mark as at the end
    if currentIndex == len(elves) - 1:
        atTheEnd = True
    else:
        atTheEnd = False

    #Amount of elves that are between the one that takes the present and the one that presents
    #are taken from - We simply split the rest of the elves (all elves beside those two) into
    #two halves and we take the smaller half (if the number of elves is not even) because
    #the task says if there are 2 opposite elves then we take the one on the left
    numberOfElvesBetweenTwoOppositeElves = math.floor((len(elves) - 2) / 2)
    #Calculate the index in the list of the elf that presents are taken from by adding
    #number of elves that are between those 2 (and +1 to acctualy get the corret elf and
    #not adress the last elf in the group inbetween) on the top of the index of the elf
    #that takes the presents
    indexOfElfThatGivesTheGifts = currentIndex + numberOfElvesBetweenTwoOppositeElves + 1
    #If the idex went out of the list just modulo it with the lenght of the list since elves
    #are sitting in the circle
    if indexOfElfThatGivesTheGifts >= len(elves):
        indexOfElfThatGivesTheGifts = indexOfElfThatGivesTheGifts % len(elves)

    #Add the amount of presents to the elf that takes them
    elves[currentIndex][1] += elves[indexOfElfThatGivesTheGifts][1]

    #Delete the elf that lost all the presents
    del elves[indexOfElfThatGivesTheGifts]

    #If current state was at the end of the list then the new state will defintely be the first
    #elemnt in the beginning since we are working with a circle of elves
    if atTheEnd:
        currentIndex = 0
    #If we removeed the elf that had index which was bigger than the current index then check
    #maybe if we are now at the end of the list, if we are go to the beginning
    elif (indexOfElfThatGivesTheGifts > currentIndex):
        if currentIndex == len(elves) -1:
            currentIndex == 0
        #Otherwise just increase the index
        else:
            currentIndex += 1
    #If we removed the element that had index which was lower than the current index then
    #we dont need to change current index because since we should always increaase it by 1
    #and we removed the element in the list that was before the current, we should decrease
    #the index by 1, and those two facts cancels each other and we are left with the same
    #index in the nest iteration
    
print("Elf {} new gets all the presents".format(elves[0][0]))
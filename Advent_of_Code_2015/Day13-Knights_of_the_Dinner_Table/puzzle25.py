# In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! 
# This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

# You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if 
# they were to find themselves sitting next to each other person. You have a circular table that will be just big enough 
# to fit everyone comfortably, and so each person will have exactly two neighbors.

# For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

# Alice would gain 54 happiness units by sitting next to Bob.
# Alice would lose 79 happiness units by sitting next to Carol.
# Alice would lose 2 happiness units by sitting next to David.
# Bob would gain 83 happiness units by sitting next to Alice.
# Bob would lose 7 happiness units by sitting next to Carol.
# Bob would lose 63 happiness units by sitting next to David.
# Carol would lose 62 happiness units by sitting next to Alice.
# Carol would gain 60 happiness units by sitting next to Bob.
# Carol would gain 55 happiness units by sitting next to David.
# David would gain 46 happiness units by sitting next to Alice.
# David would lose 7 happiness units by sitting next to Bob.
# David would gain 41 happiness units by sitting next to Carol.
# Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), 
# but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

# If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). 
# Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

#      +41 +46
# +55   David    -2
# Carol       Alice
# +60    Bob    +54
#      -7  +83
# After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

# What is the total change in happiness for the optimal seating arrangement of the actual guest list?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

import itertools

#Read input
with open(r"Day13-Knights_of_the_Dinner_Table\input.txt") as f:
    data = f.readlines()

#Variable to store all guests
guests = set()
#Dictionary that will have amount of happines gain or loss (negative gain) per people sitting next to eachother
happiness_gain_loss = dict()

#For every line in data
for information in data:
    #Remove whitespaces, last dot and then split
    information = (information.strip())[:-1].split()
    #Add guest to the set
    guests = guests | {information[0]}
    #Add amaount of happiness gain/lost to the dictionary
    if information[2] == "gain":
        happiness_gain_loss[information[0]+","+information[-1]] = int(information[3])
    else:
        happiness_gain_loss[information[0]+","+information[-1]] = -int(information[3])

#Get each possible permutation of sitting
seat_permutations = list(itertools.permutations(guests))
#Dictionaray that will have happiness score per each permutation
happiness_score = dict()

#For every permutation calculate the socre
for permutation in seat_permutations:
    happiness_score[permutation] = 0

    #For each person calculate his personal happines gain/loss and add it to the global score
    for index in range(len(permutation)):
        #For the first person look next and last person
        if index == 0:
            happiness_score[permutation] += happiness_gain_loss[permutation[index]+","+permutation[index+1]] + happiness_gain_loss[permutation[index]+","+permutation[-1]]
        #For the last person look previous and first person
        elif index == len(permutation)-1:
            happiness_score[permutation] += happiness_gain_loss[permutation[index]+","+permutation[index-1]] + happiness_gain_loss[permutation[index]+","+permutation[0]]
        #For every other person look previous and next person
        else:
            happiness_score[permutation] += happiness_gain_loss[permutation[index]+","+permutation[index+1]] + happiness_gain_loss[permutation[index]+","+permutation[index-1]]

#Sort permutations descending by score
happiness_score = dict(sorted(happiness_score.items(), key = lambda x: x[1],reverse = True))


print("Happiness for the optimal seating arrangement is",happiness_score[list(happiness_score.keys())[0]])
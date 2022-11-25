# In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty 
# apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. 
# You assume everyone else would be just as ambivalent about sitting next to you, too.

# So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

# What is the total change in happiness for the optimal seating arrangement that actually includes yourself?

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

#Add yourself to the guest set
guests = guests | {"You"}
#For each other guestt add happines gain/loss between you two to the dictionary
for guest in guests:
    happiness_gain_loss[guest+","+"You"] = 0
    happiness_gain_loss["You"+","+guest] = 0

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
# Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie 
# (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

# For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon 
# (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, 
# the best you can do in such trying circumstances.

# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

import itertools

#Read input
with open(r"Day15-Science_for_Hungry_People\input.txt") as f:
    data = f.readlines()

#Default number of teaspoons
number_of_teaspoons = 100
#Default number of calories required
calories = 500
#Variable that will save ingredients and their properties
ingredients = dict()

#For each ingredient
for ingredient in data:
    ingredient = ingredient.strip().split()

    #Save him and his properties into the dictionary
    ingredients[ingredient[0][:-1]] = [(ingredient[1],int(ingredient[2][:-1])),(ingredient[3],int(ingredient[4][:-1])),
                                        (ingredient[5],int(ingredient[6][:-1])),(ingredient[7],int(ingredient[8][:-1])),
                                        (ingredient[9],int(ingredient[10]))]

#Make every possible combination of ingredient of the size = number of teaspoons
possible_combinations = list(itertools.combinations_with_replacement(list(ingredients.keys()),number_of_teaspoons))
#Variable that will mark scores for each combination
score_per_combination = dict()

#For each combination
for combination in possible_combinations:
    #Use variable to localy sum up properties for ingredients - capacity,durability,flavor,texture and calories
    score_per_combination[combination] = [0,0,0,0,0]
    #For each ingredient in combination sum up his properties
    for ingredient in combination:
        for index in range(5):
            score_per_combination[combination][index] += ingredients[ingredient][index][1]

    #Variable that will save total score of the combination
    total_score = 1

    #If the sum of the properties bewtween ingredients is negative, make it zero
    for index in range(5):
        if score_per_combination[combination][index] < 0:
            score_per_combination[combination][index] = 0
        #Calculate contribution of property to total score if it is not calories
        if index != 4:
            total_score *= score_per_combination[combination][index]

    #Save total score into the dictionary if it has required calories
    if score_per_combination[combination][4] == calories:
        score_per_combination[combination] = total_score
    #Else remove combination from the dictionary
    else:
        score_per_combination.pop(combination,None)

#Sort combinations by score, descending
score_per_combination = dict(sorted(score_per_combination.items(), key = lambda x: x[1], reverse = True))

print("The total score of the highest-scoring cookie you can make with a calorie total of 500 is",score_per_combination[list(score_per_combination.keys())[0]])
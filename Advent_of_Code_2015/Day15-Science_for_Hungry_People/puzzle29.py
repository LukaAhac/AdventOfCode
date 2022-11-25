# Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

# Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe 
# (your puzzle input) and their properties per teaspoon:

# capacity (how well it helps the cookie absorb milk)
# durability (how well it keeps the cookie intact when full of milk)
# flavor (how tasty it makes the cookie)
# texture (how it improves the feel of the cookie)
# calories (how many calories it adds to the cookie)
# You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. 
# The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

# For instance, suppose you have these two ingredients:

# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
# Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result 
# in a cookie with the following properties:

# A capacity of 44*-1 + 56*2 = 68
# A durability of 44*-2 + 56*3 = 80
# A flavor of 44*6 + 56*-2 = 152
# A texture of 44*3 + 56*-1 = 76
# Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the 
# best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

import itertools

#Read input
with open(r"Day15-Science_for_Hungry_People\input.txt") as f:
    data = f.readlines()

#Default number of teaspoons
number_of_teaspoons = 100
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
    #Use variable to localy sum up properties for ingredients - capacity,durability,flavor,texture
    score_per_combination[combination] = [0,0,0,0]
    #For each ingredient in combination sum up his properties
    for ingredient in combination:
        for index in range(4):
            score_per_combination[combination][index] += ingredients[ingredient][index][1]

    #Variable that will save total score of the combination
    total_score = 1

    #If the sum of the properties bewtween ingredients is negative, make it zero
    for index in range(4):
        if score_per_combination[combination][index] < 0:
            score_per_combination[combination][index] = 0
        #Calculate contribution of property to total score
        total_score *= score_per_combination[combination][index]

    #Save total score into the dictionary
    score_per_combination[combination] = total_score

#Sort combinations by score, descending
score_per_combination = dict(sorted(score_per_combination.items(), key = lambda x: x[1], reverse = True))

print("The total score of the highest-scoring cookie you can make is",score_per_combination[list(score_per_combination.keys())[0]])
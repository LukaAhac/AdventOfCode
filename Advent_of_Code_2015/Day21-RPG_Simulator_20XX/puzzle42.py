# Turns out the shopkeeper is working with the boss, and can persuade you to buy whatever items he wants. The other rules still apply, 
# and he still only has one of each item.

# What is the most amount of gold you can spend and still lose the fight?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

import itertools

#Read input
with open(r"Day21-RPG_Simulator_20XX\input.txt") as f:
    data = f.readlines()

#Load boss data from input
boss_hit_points = int(data[0].strip().split()[2])
boss_dmg = int(data[1].strip().split()[1])
boss_armour = int(data[2].strip().split()[1])
#Player hit points
player_hit_points = 100
#Availible weapons
weapons =  {"Dagger" : (8,4,0),
            "Shortsword" : (10,5,0),
            "Warhammer" : (25,6,0),
            "Longsword" : (40,7,0),
            "Greataxe" : (74,8,0)}
#Availible armour
armour =   {"Leather" : (13,0,1),
            "Chainmail" : (31,0,2),
            "Splintmail" : (53,0,3),
            "Bandedmail" : (75,0,4),
            "Platemail" : (102, 0,5)}
#Availible rings
rings = {"Damage +1" : (25,1,0),
        "Damage +2" : (50,2,0),
        "Damage +3" : (100,3,0),
        "Defense +1" : (20,0,1),
        "Defense +2" : (40,0,2),
        "Defense +3" : (80,0,3)}

#Each weapon combination you can buy
weapon_combinations = list(weapons.keys())

#Add "None" to armour dic as representation of no armour bought
armour["None"] = (0,0,0)
#Each armour combination you can buy
armour_combinations = list(armour.keys())

#Variable to hold each weapon and armour combination you can buy
weapon_and_armour_combinations = []
#Make each weapon and armour combination
for wep in weapon_combinations:

    for arm in armour_combinations:

        weapon_and_armour_combinations.append([wep,arm])

#Add two "None" rings as representation of 0 or just 1 rings bought - This creates few repeating gear combinatiosn leater
#but since we are working with small amount of data it doenst matter
rings["None1"] = (0,0,0)
rings["None2"] = (0,0,0)
#Each rings combination you can buy
rings_combinations = list(itertools.combinations(rings.keys(),2))

#Variable to hold each weapon,armour and rings combination you can buy
weapon_armour_and_rings_combinations = []
#Make each weapon, armour and ring combination
for weapon_and_armour in weapon_and_armour_combinations:

    for rng in rings_combinations:

        weapon_armour_and_rings_combinations.append(weapon_and_armour+list(rng))

#Set best combination to "None"
best_combination = None
#Set best price to 0 - 0 because we are now looking for most expensive gear that would still make u lose
best_price = 0

#For each combination
for combination in weapon_armour_and_rings_combinations:

    #Sum up the price of gear
    price = weapons[combination[0]][0] + armour[combination[1]][0] + rings[combination[2]][0] + rings[combination[3]][0]
    #Sum up the amount of DMG that gear provides
    playerDMG = weapons[combination[0]][1] + armour[combination[1]][1] + rings[combination[2]][1] + rings[combination[3]][1]
    #Sum up the amount of armour that gear provides
    playerArmour = weapons[combination[0]][2] + armour[combination[1]][2] + rings[combination[2]][2] + rings[combination[3]][2]

    #If gear price is higher than the best price check if you lose against boss
    if price > best_price:

        #Initialize boss HP to
        bossHP = boss_hit_points
        #Initialize player HP
        playerHP = player_hit_points
        #Calculate boss DMG considering player armour
        bossDMG_per_turn = boss_dmg - playerArmour 
        if bossDMG_per_turn <= 0:
            bossDMG_per_turn = 1
        #Calculate player DMG considering boss armour
        playerDMG_per_turn = playerDMG - boss_armour
        if playerDMG_per_turn <= 0:
            playerDMG_per_turn = 1

        #Until someone dies
        while True:

            #Player strikes first
            bossHP -= playerDMG_per_turn
            #If boss is dead, player won
            if bossHP <= 0:
                playerWON = True
                break
            
            #Boss strikes second
            playerHP -= bossDMG_per_turn
            #If player died, boss won
            if playerHP <= 0:
                playerWON = False
                break

        #If player lost, set new best combination and new best price
        if not playerWON:
            best_combination = combination
            best_price = price

print(best_price,"is the most amount of gold you can spend and still lose the fight.")
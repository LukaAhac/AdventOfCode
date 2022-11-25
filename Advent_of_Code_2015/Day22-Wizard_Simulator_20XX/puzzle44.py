# On the next run through the game, you increase the difficulty to hard.

# At the start of each player turn (before any other effects apply), you lose 1 hit point. If this brings you to or below 0 hit points, you lose.

# With the same starting stats for you and the boss, what is the least amount of mana you can spend and still win the fight?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day22-Wizard_Simulator_20XX\input.txt") as f:
    data = f.readlines()

#Initialize boss HP from input
boss_hit_points = int(data[0].strip().split()[2])
#Initialize boss dmg from input
boss_dmg = int(data[1].strip().split()[1])
#Initialize player HP
player_hit_points = 50
#Initialize player mana
player_mana = 500
#Initialize possible spells
spells = ["Magic Missile","Drain","Shield","Poison","Recharge"]

#Class that will remember the state of the game
#Idea is that each time player is on a turn, we fork the game for every possible outcome and class saves the state of each outcome
class Game_state():

    def __init__(self,bossHP,playerHP,playerMana,mana_spent,effects,timers):

        self.bossHP = bossHP
        self.playerHP = playerHP
        self.playerMana = playerMana
        self.mana_spent = mana_spent
        self.effects = effects
        self.timers = timers

#Initialize least amount of mana for win to something big
least_amout_of_mana_win = 10000

#List of the game states
states = []
#Simulte first player turn - fork game for each possible spell, applay -1 HP aswell
#Cast Magic Missile
states.append(Game_state(boss_hit_points-4,player_hit_points-1,player_mana-53,53,[],[]))
#Cast Drain
states.append(Game_state(boss_hit_points-2,player_hit_points+1,player_mana-73,73,[],[]))
#Cast Shield
states.append(Game_state(boss_hit_points,player_hit_points-1,player_mana-113,113,["Shield"],[6]))
#Cast Poison
states.append(Game_state(boss_hit_points,player_hit_points-1,player_mana-173,173,["Poison"],[6]))
#Cast Recharge
states.append(Game_state(boss_hit_points,player_hit_points-1,player_mana-229,229,["Recharge"],[5]))

#Loop until there are unfinished game
while len(states) > 0:

    #Variable that will save new game states
    new_states = []

    #For each state play 2 turns (first boss turn, then player turn - that is the reason 
    # there was simulated first player turn earlier, because code starts with boss turn - its simpler)
    for state in states:

        #Initialize player armour to 0
        armour = 0

        #Trigger casted effects
        for index in range(len(state.effects)):
            
            if state.effects[index] == "Shield":
                armour = 7
            elif state.effects[index] == "Poison":
                state.bossHP -= 3
            elif state.effects[index] == "Recharge":
                state.playerMana += 101
            #Reduce effect timer
            state.timers[index] -= 1

        #If boss died after effect trigger (poison)
        if state.bossHP <= 0:
            #If that is least mana spent win
            if state.mana_spent < least_amout_of_mana_win:
                #Save amount of new least mana win
                least_amout_of_mana_win = state.mana_spent
            #Continue to next game state
            continue

        #If there are effects that expired (timer = 0), remove them
        for index in range(len(state.timers)):
            if state.timers[index] <= 0:
                state.effects.pop(index)
        #Also, remove zeros from timers
        state.timers = list(filter(lambda x: x != 0, state.timers))

        #Boss deals dmg - BOSS turn
        state.playerHP -= (boss_dmg - armour)

        #If player died after boss dealt dmg, cotinue to the next game state
        if state.playerHP <= 0:
            continue

        #Player turn starts, set armour to 0
        armour = 0

        #Hard mode - reduce player HP by 1
        state.playerHP -= 1
        #If player died to that, continue to next state
        if state.playerHP <= 0:
            continue

        #Trigger casted effects
        for index in range(len(state.effects)):
            
            if state.effects[index] == "Shield":
                armour = 7
            elif state.effects[index] == "Poison":
                state.bossHP -= 3
            elif state.effects[index] == "Recharge":
                state.playerMana += 101
            #Reduce effect timer
            state.timers[index] -= 1

        #If boss died after effect trigger (poison)
        if state.bossHP <= 0:
            #If that is least mana spent win
            if state.mana_spent < least_amout_of_mana_win:
                #Save amount of new least mana win
                least_amout_of_mana_win = state.mana_spent
            #Continue to next game state
            continue

        #If there are effects that expired (timer = 0), remove them
        for index in range(len(state.timers)):
            if state.timers[index] <= 0:
                state.effects.pop(index)
        #Also, remove zeros from timers
        state.timers = list(filter(lambda x: x != 0, state.timers))


        #Fork game for each possible spell that player can cast
        for spell in spells:

            #If spell is not one of the effects that is already active, cast it
            if spell not in state.effects:

                #If spell is Magic Missile
                if spell == "Magic Missile":

                    #If player would fall under 53 mana after cast (in that case he lost, because he will not be able to cast spell next turn) 
                    #or amount of mana spent would go beyond best mana spent win found, continue to the next state
                    if (state.playerMana - 53) < 53 or (state.mana_spent + 53) > least_amout_of_mana_win:
                        continue
                    #If boss would die after cast, save if it is the least mana win and continue to the next state
                    elif (state.bossHP-4) <= 0:
                        if (state.mana_spent + 53) < least_amout_of_mana_win:
                            least_amout_of_mana_win = state.mana_spent + 53
                        continue
                    #Cast Magice Missile and create new game state
                    else:
                        new_states.append(Game_state(state.bossHP-4,state.playerHP,state.playerMana-53,state.mana_spent+53,state.effects.copy(),state.timers.copy()))

                elif spell == "Drain":

                    #If player would fall under 53 mana after cast (in that case he lost, because he will not be able to cast spell next turn) 
                    #or amount of mana spent would go beyond best mana spent win found, continue to the next state
                    if (state.playerMana - 73) < 53 or (state.mana_spent + 73) > least_amout_of_mana_win:
                        continue
                    #If boss would die after cast, save if it is the least mana win and continue to the next state
                    elif (state.bossHP-2) <= 0:
                        if (state.mana_spent + 73) < least_amout_of_mana_win:
                            least_amout_of_mana_win = state.mana_spent + 73
                        continue
                    #Cast Drain and create new game state
                    else:
                        new_states.append(Game_state(state.bossHP-2,state.playerHP+2,state.playerMana-73,state.mana_spent+73,state.effects.copy(),state.timers.copy()))

                elif spell == "Shield":

                    #If player would fall under 53 mana after cast (in that case he lost, because he will not be able to cast spell next turn) 
                    #or amount of mana spent would go beyond best mana spent win found, continue to the next state
                    if (state.playerMana - 113) < 53 or (state.mana_spent + 113) > least_amout_of_mana_win:
                        continue
                    #Cast Shield and create new game state
                    else:
                        new_states.append(Game_state(state.bossHP,state.playerHP,state.playerMana-113,state.mana_spent+113,
                                            state.effects.copy(),state.timers.copy()))
                        new_states[-1].effects.append("Shield")
                        new_states[-1].timers.append(6)

                elif spell == "Poison":

                    #If player would fall under 53 mana after cast (in that case he lost, because he will not be able to cast spell next turn) 
                    #or amount of mana spent would go beyond best mana spent win found, continue to the next state
                    if (state.playerMana - 173) < 53 or (state.mana_spent + 173) > least_amout_of_mana_win:
                        continue
                    #Cast Poison and create new game state
                    else:
                        new_states.append(Game_state(state.bossHP,state.playerHP,state.playerMana-173,state.mana_spent+173,
                                            state.effects.copy(),state.timers.copy()))
                        new_states[-1].effects.append("Poison")
                        new_states[-1].timers.append(6)

                elif spell == "Recharge":

                    #If player would fall under 53 mana after cast (in that case he lost, because he will not be able to cast spell next turn) 
                    #or amount of mana spent would go beyond best mana spent win found, continue to the next state
                    if (state.playerMana - 229) < 53 or (state.mana_spent + 229) > least_amout_of_mana_win:
                        continue
                    #Cast Recharge and create new game state
                    else:
                        new_states.append(Game_state(state.bossHP,state.playerHP,state.playerMana-229,state.mana_spent+229,
                                            state.effects.copy(),state.timers.copy()))
                        new_states[-1].effects.append("Recharge")
                        new_states[-1].timers.append(5)

    #Load new states into states for next iteration
    states = new_states

print(least_amout_of_mana_win,"is the least amount of mana you can spend and still win the fight")
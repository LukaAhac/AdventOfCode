# Now that you're warmed up, it's time to play the real game.

# A second compartment opens, this time labeled Dirac dice. Out of it falls a single three-sided die.

# As you experiment with the die, you feel a little strange. An informational brochure in the compartment 
# explains that this is a quantum die: when you roll it, the universe splits into multiple copies, 
# one copy for each possible outcome of the die. In this case, rolling the die always splits the universe 
# into three copies: one where the outcome of the roll was 1, one where it was 2, and one where it was 3.

# The game is played the same as before, although to prevent things from getting too far out of hand, the game now 
# ends when either player's score reaches at least 21.

# Using the same starting positions as in the example above, player 1 wins in 444356092776315 universes, 
# while player 2 merely wins in 341960390180808 universes.

# Using your given starting positions, determine every possible outcome. Find the player that wins in more universes; 
# in how many universes does that player win?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day21-Dirac_Dice\input.txt") as f:
    data = f.readlines()
    
#Given input
inp = []

#Parse input
for line in data:
    line = line.strip()
    inp.append(line)

#Player 1 score and position
p1_score = 0
p1_position = int(inp[0][-1])
#Player 2 score and position
p2_score = 0
p2_position = int(inp[1][-1])


#Make the dictionary of all possible outcomes of rolling a 3-sided dice
#Keys are possible outcomes(sum of the die values) while values are number of occurences
possible_tosses = dict()

for t1 in range(3):

    for t2 in range(3):

        for t3 in range(3):

            if t1+t2+t3+3 not in possible_tosses:
                possible_tosses[t1+t2+t3+3] = 1
            else:
                possible_tosses[t1+t2+t3+3]  += 1

#List to track a number of wins po each player
#Player 1 has index 0 and player 2 has index 1
winners = [0,0]

#Dictionary of all current games across all created universes
#Keys are tuple of game states (P1_Position,P1_Score,P2_Position,P2_score,indexOfPlayerToTakeNextTurn)
games = dict()
#Initially we start with just one game beinh palyed in one universe
games[(p1_position,p1_score,p2_position,p2_score,0)] = 1

#Until all games have been finished play games
while len(games) > 0:

    #Dictionary of the game states for the next turn
    nextGames = dict()

    #For each game state callculate its next game states
    for g in games.keys():
        
        #For each possible outcome perform a turn for a current game state
        for pt in possible_tosses.keys():

            #Mock state that we will fill to form a next state
            mockState = [0,0,0,0,0]

            #Player 1 on a turn
            if g[4] == 0:

                #Calculate position and score just like in part 1
                mockState[0] = g[0] + pt
                while mockState[0] > 10:
                    mockState[0] -= 10
                mockState[1] = g[1] + mockState[0]
                mockState[4] = 1

                #Copy player 2 state
                mockState[2] = g[2]
                mockState[3] = g[3]

                #If player 1 won
                if mockState[1] >= 21:
                    #Increase its win counter by the times of that game state that have 
                    #happened times number of times that particular outcome happens
                    winners[0] += games[g] * possible_tosses[pt]
                #If it did not win just create next game states, where there will be (number of that particular game state
                #occurrence times number of current outcome occurance) times that game state occurs
                else:

                    tpl = tuple(mockState)
                    if tpl in nextGames:
                        nextGames[tpl] += games[g] * possible_tosses[pt]
                    else:
                        nextGames[tpl] = games[g] * possible_tosses[pt]
            #Player 2 on a turn
            else:

                #Calculate position and score just like in part 1
                mockState[2] = g[2] + pt
                while mockState[2] > 10:
                    mockState[2] -= 10
                mockState[3] = g[3] + mockState[2]
                mockState[4] = 0

                #Copy player 1 state
                mockState[0] = g[0]
                mockState[1] = g[1]

                #If player won increase his number of wins just like for player 1
                if mockState[3] >= 21:

                    winners[1] += games[g] * possible_tosses[pt]
                #Else create new game statest just like for player 1
                else:

                    tpl = tuple(mockState)
                    if tpl in nextGames:
                        nextGames[tpl] += games[g] * possible_tosses[pt]
                    else:
                        nextGames[tpl] = games[g] * possible_tosses[pt]
    games = nextGames


print("That player wins in {} universes".format(winners[0] if winners[0] > winners[1] else winners[1]))
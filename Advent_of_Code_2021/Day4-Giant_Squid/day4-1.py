# You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see 
# any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

# Maybe it wants to play bingo?

# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, 
# and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) 
# If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

# The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. 
# It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). 
# For example:

# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
# After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked 
# as follows (shown here adjacent to each other to save space):

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# Finally, 24 is drawn:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# At this point, the third board wins because it has at least one complete row or column of marked numbers 
# (in this case, the entire top row is marked: 14 21 17 24 4).

# The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on 
# that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when 
# the board won, 24, to get the final score, 188 * 24 = 4512.

# To guarantee victory against the giant squid, figure out which board will win first. What will your final 
# score be if you choose that board?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day4-Giant_Squid\input.txt") as f:
    data = f.readlines()

#Given input
inp = []

#Parse input
for line in data:
    line = line.strip()
    inp.append(line)

#Numbers to drow are in the first row of an input
nums = inp[0]
#Boards are given in the input from the second row up to the end
boards = inp[2:]

#List for structured bingo boards
allBingoBoards = list()

#Strcure the board into the list of bingo board rows
#We know that there is (lenght of the board list + 1) / 6 boards, becasue each board takes 5 rows of the input
#and then there is an empty row betwen them, +1 is there to add up for the row after the last board which is not
#in the list
for index in range(int((len(boards)+1)/6)):

    newBoard = []

    for index1 in range(5):
        newBoard.append(boards[index*6+index1].split())

    allBingoBoards.append(newBoard)

#List of drawing numbers
numbers = nums.split(",")

#Go thorught numbers to draw
for drawnNumber in numbers:

    #Then go tgrough all the boards
    for board in allBingoBoards:

        #Go throught board rows
        for row in board:

            #If the drawn number is in the row
            if drawnNumber in row:
                #Mark it
                ind = row.index(drawnNumber)
                row[ind] = row[ind] + "M"
                
    #Then go throught the board to check if there is a winner
    for board in allBingoBoards:

        #Initially set winner flag to False
        winner = False

        #For the each row of the board
        for row in board:

            #Check if all of the numbers in the row are marked
            marked = list(filter(lambda x: x[-1] == "M",row))
            #There are 5 numbers in the row, and if they are marked we have a winner
            if len(marked) == 5:
                winner = True
            
        #For each column of the board
        for col in range(5):

            #Construct the list out of the column
            column = [board[0][col],board[1][col],board[2][col],board[3][col],board[4][col]]

            #If the whole column is marked
            marked = list(filter(lambda x: x[-1] == "M",column))
            #We have a winner
            if len(marked) == 5:
                winner = True

        #If we have a winner
        if winner:

            #Sum of unmarked number
            unmarkedSum = 0

            #Go through the winning board
            for row in board:

                for num in row:

                    #Sum all unmarked numbers
                    if num[-1] != "M":
                        unmarkedSum += int(num)
            #Output
            print("If I choose that board my final score will be:",unmarkedSum*int(drawnNumber))
            quit()
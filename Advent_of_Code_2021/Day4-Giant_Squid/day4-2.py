# On the other hand, it might be wise to try a different strategy: let the giant squid win.

# You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time 
# counting its arms, the safe thing to do is to figure out which board will win last and choose that one. 
# That way, no matter which boards it picks, it will win for sure.

# In the above example, the second board is the last to win, which happens after 13 is eventually called and 
# its middle column is completely marked. If you were to keep playing until this point, the second board would 
# have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

# Figure out which board will win last. Once it wins, what would its final score be?

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

    #Remaining boards
    newBoards = []
                
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

            #Mark is to be the last winner
            lastWinner = board
            #Mak the number with which the winner was drawn
            lastDraw = drawnNumber

        else:
            
            #If the board is not winning borad, keep it
            newBoards.append(board)

        #Keep only boards that did not win
        allBingoBoards = newBoards


 #Sum of unmarked number
unmarkedSum = 0

#Go through the last winning board
for row in lastWinner:

    for num in row:

        #Sum all unmarked numbers
        if num[-1] != "M":
            unmarkedSum += int(num)
#Output
print("Its final score will be:",unmarkedSum*int(lastDraw))
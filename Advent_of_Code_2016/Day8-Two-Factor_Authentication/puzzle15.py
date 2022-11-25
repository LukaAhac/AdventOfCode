# You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

# To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

# Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works.
#  Now you just have to work out what the screen would have displayed.

# The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. 
# The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

# rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
# rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off 
# the right end appear at the left end of the row.
# rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall 
# off the bottom appear at the top of the column.
# For example, here is a simple sequence on a smaller screen:

# rect 3x2 creates a small rectangle in the top-left corner:

# ###....
# ###....
# .......
# rotate column x=1 by 1 rotates the second column down by one pixel:

# #.#....s
# ###....
# .#.....
# rotate row y=0 by 4 rotates the top row right by four pixels:

# ....#.#
# ###....
# .#.....
# rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

# .#..#.#
# #.#....
# .#.....
# As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. 
# That's what the advertisement on the back of the display tries to convince you, anyway.

# There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, 
# how many pixels should be lit?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
from collections import deque

#Read input
with open(r"Day8-Two-Factor_Authentication\input.txt") as f:
    data = f.readlines()

#List of the instructions
instructions = []

#Preprocess the data
for line in data:
    instructions.append(line.strip())

#Creating a list that will act as a LCD display
LCD_display_row = ["."]*50
LCD_display = []
for _ in range(6):
    LCD_display.append(LCD_display_row.copy())

#For each instruction
for inst in instructions:

    #Split it by spaces
    inst = inst.split()

    #If the instrucion is rect
    if inst[0] == "rect":

        #Get width and height of a rectangle
        width,height = map(int,inst[1].split("x"))

        #Turn the required pixels ON
        for row in range(height):

            LCD_display[row][:width] = ["#"]*width

    #If the instruction is rotate row
    elif inst[0] == "rotate" and inst[1] == "row":

        #Get the row
        row = int(inst[2].split("=")[1])
        #Rotate the row
        newList = deque(LCD_display[row])
        newList.rotate(int(inst[4]))
        #Put the rotated row in the display
        LCD_display[row] = list(newList)

    #If the instruction is rotate column
    elif inst[0] == "rotate" and inst[1] == "column":

        #Get the column
        column = int(inst[2].split("=")[1])

        #Convert the column into one list
        listOfTheColumn = []
        for row in LCD_display:
            listOfTheColumn.append(row[column])

        #Rotate the column
        listOfTheColumn = deque(listOfTheColumn)
        listOfTheColumn.rotate(int(inst[4]))

        #Put the column in the display
        for index in range(len(LCD_display)):
            LCD_display[index][column] = listOfTheColumn[index]

#Lit pixels counter
lit_pixels = 0

#Count the lit pixels
for row in LCD_display:
    lit_pixels += row.count("#")

print(lit_pixels,"pixels should be lit!")

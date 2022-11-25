# You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

# After you swipe your card, what code is the screen trying to display?

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

for letterIndex in range(10):

    for rowIndex in range(6):

        print(LCD_display[rowIndex][letterIndex*5:letterIndex*5+5])

    print()

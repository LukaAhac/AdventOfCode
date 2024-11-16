from Utils.utils import readThisPuzzlesInput
from collections import defaultdict

lines = readThisPuzzlesInput(__file__)

def calculateFromColumnIndex(beginIndex):
    return beginIndex - 1  if beginIndex - 1 >= 0 else 0

def calculateEndColummnIndex(endIndex, currentRow):
    return endIndex + 1  if endIndex + 1 < len(currentRow) else len(currentRow) - 1

def isSymbol(char):
    if not char.isdigit() and char != '.':
        return True
    return False

partOneSum = 0
partTwoSum = 0

grid = [list(line) for line in lines]
gears = defaultdict(list)

for rowIndex in range(0, len(grid)):
    columnBeginIndex = -1
    columnEndIndex = -1
    isInsideNumber = False

    for columnIndex in range(0, len(grid[rowIndex])):
        char = grid[rowIndex][columnIndex]
        if not isInsideNumber and char.isdigit():
            columnBeginIndex = columnIndex
            isInsideNumber = True
        if isInsideNumber and not char.isdigit():
            columnEndIndex = columnIndex - 1
            isInsideNumber = False
        if isInsideNumber and columnIndex == (len(grid[rowIndex]) - 1):
            columnEndIndex = columnIndex
            isInsideNumber = False

        if columnBeginIndex != -1 and columnEndIndex != -1:

            numberAsString = ""
            for j in range(columnBeginIndex, columnEndIndex + 1):
                numberAsString += grid[rowIndex][j]
            number = int(numberAsString)

            isAdjecent = False

            if rowIndex > 0:
                fromColumn = calculateFromColumnIndex(columnBeginIndex)
                toColumn = calculateEndColummnIndex(columnEndIndex, grid[rowIndex])

                for j in range(fromColumn, toColumn + 1):
                    if isSymbol(grid[rowIndex-1][j]):
                        isAdjecent = True
                        if grid[rowIndex-1][j] == '*':
                            gears[(rowIndex-1,j)].append(number)

            if columnBeginIndex > 0:
                if isSymbol(grid[rowIndex][columnBeginIndex - 1]):
                    isAdjecent = True
                    if grid[rowIndex][columnBeginIndex - 1] == '*':
                        gears[(rowIndex,columnBeginIndex - 1)].append(number)

            if columnEndIndex < len(grid[rowIndex]) - 1:
                if isSymbol(grid[rowIndex][columnEndIndex + 1]):
                    isAdjecent = True
                    if grid[rowIndex][columnEndIndex + 1] == '*':
                        gears[(rowIndex,columnEndIndex + 1)].append(number)

            if rowIndex < len(grid) - 1:
                fromColumn = calculateFromColumnIndex(columnBeginIndex)
                toColumn = calculateEndColummnIndex(columnEndIndex, grid[rowIndex])

                for j in range(fromColumn, toColumn + 1):
                    if isSymbol(grid[rowIndex+1][j]):
                        isAdjecent = True
                        if grid[rowIndex+1][j] == '*':
                            gears[(rowIndex+1,j)].append(number)

            if isAdjecent:
                partOneSum += number

            columnBeginIndex = -1
            columnEndIndex = -1

for numberList in gears.values():
    if len(numberList) == 2:
        partTwoSum += numberList[0]*numberList[1]

print(partOneSum)
print(partTwoSum)
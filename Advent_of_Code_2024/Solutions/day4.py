from Utils.utils import readThisPuzzlesInput

lines = readThisPuzzlesInput(__file__)

grid = lines
directions = [(-1, 0), (-1 ,1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
word = "XMAS"

partOneSum = 0
partTwoSum = 0

def checkForXmas(rowIndex, columnIndex, direction):
    for i in range(0, len(word)):
        if not 0 <= rowIndex < len(grid) or not 0 <= columnIndex < len(grid[0]):
            return False
        
        if grid[rowIndex][columnIndex] != word[i]:
            return False
        
        rowIndex += direction[0]
        columnIndex += direction[1]
        
    return True

for rowIndex in range(0, len(grid)):
    row = grid[rowIndex]
    columnIndex = row.find('X')

    while 0 <= columnIndex < len(row):
        for direction in directions:
            if checkForXmas(rowIndex, columnIndex, direction):
                partOneSum += 1

        columnIndex = row.find('X', columnIndex + 1)

def checkForXShapedMases(rowIndex, columnIndex):
    def cellsContainMAndS(cell1, cell2):
        return cell1 == 'M' and cell2 == 'S' or cell1 == 'S' and cell2 == 'M'

    if not cellsContainMAndS(grid[rowIndex - 1][columnIndex - 1], grid[rowIndex + 1][columnIndex + 1]):
        return False

    if not cellsContainMAndS(grid[rowIndex - 1][columnIndex + 1], grid[rowIndex + 1][columnIndex - 1]):
        return False

    return True

for rowIndex in range(1, len(grid) - 1):
    row = grid[rowIndex]
    columnIndex = row.find('A', 1)

    while 1 <= columnIndex < len(row) - 1:
        if checkForXShapedMases(rowIndex, columnIndex):
            partTwoSum += 1

        columnIndex = row.find('A', columnIndex + 1)

print(partOneSum)
print(partTwoSum)
from Utils.utils import readThisPuzzlesInput

lines = readThisPuzzlesInput(__file__)

grid = [list(line) for line in lines]
guardRow = -1
guardColumn = -1

for rowIndex in range(0, len(grid)):
    if grid[rowIndex].count("^") > 0:
        guardRow = rowIndex
        guardColumn = grid[rowIndex].index("^")
        break

partOneSum = 0
partTwoSum = 0

def calculateGuardMovement(grid, guardRow, guardColumn):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    currentDirectionIndex = 0
    turningPoints = []

    while(True):
        grid[guardRow][guardColumn] = "X"

        nextGuardRow = guardRow + directions[currentDirectionIndex][0]
        nextGuardColumn = guardColumn + directions[currentDirectionIndex][1]

        if not 0 <= nextGuardRow < len(grid) or not 0 <= nextGuardColumn < len(grid[0]):
            uniquePlacesGuardVisited = 0
            for line in grid:
                uniquePlacesGuardVisited += line.count("X")
            return (True, uniquePlacesGuardVisited)

        if grid[nextGuardRow][nextGuardColumn] != "#":
            guardRow = nextGuardRow
            guardColumn = nextGuardColumn
        else:
            if turningPoints.count((guardRow, guardColumn, currentDirectionIndex)) > 0:
                return (False, 0)
            turningPoints.append((guardRow, guardColumn, currentDirectionIndex))
            currentDirectionIndex = (currentDirectionIndex + 1) % len(directions)

partOneSum = calculateGuardMovement(grid, guardRow, guardColumn)[1]

for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        if grid[i][j] != "#" and not (i == guardRow and j == guardColumn):
            grid[i][j] = "#"
            isGuardLooped = not calculateGuardMovement(grid, guardRow, guardColumn)[0]
            grid[i][j] = "."

            if(isGuardLooped):
                partTwoSum += 1

print(partOneSum)
print(partTwoSum)
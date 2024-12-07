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

def calculateGuardMovement(grid, guardRow, guardColumn, isFirstPart):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    currentDirectionIndex = 0
    turningPoints = []
    guardPathCoordinates = set()

    while(True):
        grid[guardRow][guardColumn] = "X"
        if isFirstPart:
            guardPathCoordinates.add((guardRow, guardColumn))

        nextGuardRow = guardRow + directions[currentDirectionIndex][0]
        nextGuardColumn = guardColumn + directions[currentDirectionIndex][1]

        if not 0 <= nextGuardRow < len(grid) or not 0 <= nextGuardColumn < len(grid[0]):
            if isFirstPart:
                uniquePlacesGuardVisited = 0
                for line in grid:
                    uniquePlacesGuardVisited += line.count("X")
                return (False, uniquePlacesGuardVisited, guardPathCoordinates)
            else:
                return (False, 0, {})
            
        if grid[nextGuardRow][nextGuardColumn] != "#":
            guardRow = nextGuardRow
            guardColumn = nextGuardColumn
        else:
            if turningPoints.count((guardRow, guardColumn, currentDirectionIndex)) > 0:
                return (True, 0, {})
            turningPoints.append((guardRow, guardColumn, currentDirectionIndex))
            currentDirectionIndex = (currentDirectionIndex + 1) % len(directions)

guardLooped, partOneSum, guardPathCoordinates = calculateGuardMovement(grid, guardRow, guardColumn, True)

guardPathCoordinates.remove((guardRow, guardColumn))
for guardPathCoordinate in guardPathCoordinates:
    grid[guardPathCoordinate[0]][guardPathCoordinate[1]] = "#"
    isGuardLooped = calculateGuardMovement(grid, guardRow, guardColumn, False)[0]
    grid[guardPathCoordinate[0]][guardPathCoordinate[1]] = "."

    if isGuardLooped:
        partTwoSum += 1

print(partOneSum)
print(partTwoSum)
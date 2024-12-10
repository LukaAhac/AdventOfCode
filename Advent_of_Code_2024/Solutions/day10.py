from Utils.utils import readThisPuzzlesInput

lines = readThisPuzzlesInput(__file__)

grid = []

for line in lines:
    grid.append([int(x) for x in list(line)])

trailheads = []

for rowIndex in range(0, len(grid)):
    for columnIndex in range(0, len(grid[rowIndex])):
        if grid[rowIndex][columnIndex] == 0:
            trailheads.append((rowIndex, columnIndex))

def findPeak(r, c, lastHeight):
    if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]):
        return []
    
    currentHeight = grid[r][c]
    
    if currentHeight != lastHeight + 1:
        return []
    
    if grid[r][c] == 9:
        return [(r,c)]
    
    return findPeak(r + 1, c, currentHeight) + findPeak(r - 1, c, currentHeight) + findPeak(r, c + 1, currentHeight) + findPeak(r, c - 1, currentHeight)

partOneSum = 0
partTwoSum = 0

for trailhead in trailheads:
    peaks = findPeak(trailhead[0], trailhead[1], -1)

    partOneSum += len(set(peaks))
    partTwoSum += len(peaks)

print(partOneSum)
print(partTwoSum)
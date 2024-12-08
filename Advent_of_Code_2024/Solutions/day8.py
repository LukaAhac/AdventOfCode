from Utils.utils import readThisPuzzlesInput
from collections import defaultdict

lines = readThisPuzzlesInput(__file__)

grid = lines
antennas = defaultdict(list)

lastRow = len(grid) - 1
lastColumn = len(grid[0]) - 1

for row in range(0, len(grid)):
    for column in range(0, len(grid[row])):
        if grid[row][column] != '.':
            antennas[grid[row][column]].append((row, column))

partOneAntinodes = set()
partTwoAntinodes = set()

for locations in antennas.values():
    for location1 in locations:
        for location2 in locations:

            if location1 == location2:
                continue

            diff = (location2[0] - location1[0], location2[1] - location1[1])
            antinodesCounter = 0

            antinode = location2
            while(0 <= antinode[0] <= lastRow and 0 <= antinode[1] <= lastColumn):
                partTwoAntinodes.add(antinode)

                if antinodesCounter == 1:
                    partOneAntinodes.add(antinode)

                antinodesCounter += 1

                antinode = (antinode[0] + diff[0], antinode[1] + diff[1])

print(len(partOneAntinodes))
print(len(partTwoAntinodes))
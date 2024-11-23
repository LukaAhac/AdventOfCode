from Utils.utils import readThisPuzzlesInput

lines = readThisPuzzlesInput(__file__)

initialSeedNumbers = [int(x) for x in lines[0].split(":")[1].split()]
maps = []

mapLines = []
for line in lines[2:]:
    if "map" in line:
        mapLines = []
        continue
    elif line == "":
        maps.append(mapLines)
    else:
        mapLines.append([int(x) for x in line.split()])
maps.append(mapLines)

seedNumberRangesPartOne = []
for seedNumber in initialSeedNumbers:
    seedNumberRangesPartOne.append((seedNumber, seedNumber))

seedNumberRangesPartTwo = []
for i in range(0, int(len(initialSeedNumbers)/2)):
    seedNumberRangesPartTwo.append((initialSeedNumbers[i*2],initialSeedNumbers[i*2]+initialSeedNumbers[i*2+1]-1))

def translateRange(range, mapping):
    return (range[0] - mapping[1] + mapping[0], range[1] - mapping[1] + mapping[0])

def getLowestLocationNumber(seedNumberRanges, maps):
    for map in maps:
        newSeedNumberRanges = []
        for mapping in map:
            newRanges = []
            for range in seedNumberRanges:
                mappingRange = (mapping[1], mapping[1] + mapping[2] - 1)
                #Mappings outside of the range
                if mappingRange[1] < range[0] or mappingRange[0] > range[1]:
                    newRanges.append(range)
                #Mapping covers whole range
                elif mappingRange[0] <= range[0] and mappingRange[1] >= range[1]:
                    newSeedNumberRanges.append(translateRange(range, mapping))
                #Mapping covers left part of the range
                elif mappingRange[0] <= range[0] and mappingRange[1] < range[1]:
                    newSeedNumberRanges.append(translateRange((range[0],mappingRange[1]), mapping))
                    newRanges.append((mappingRange[1] + 1, range[1]))
                #Mapping covers right part of the range
                elif mappingRange[0] > range[0] and mappingRange[1] >= range[1]:
                    newSeedNumberRanges.append(translateRange((mappingRange[0],range[1]), mapping))
                    newRanges.append((range[0], mappingRange[0]-1))
                #Mapping covers middle part of the range
                elif mappingRange[0] > range[0] and mappingRange[1] < range[1]:
                    newSeedNumberRanges.append(translateRange(mappingRange, mapping))
                    newRanges.append((range[0], mappingRange[0] - 1))
                    newRanges.append((mappingRange[1] + 1, range[1]))

            seedNumberRanges = newRanges
        seedNumberRanges.extend(newSeedNumberRanges)
    seedNumberRanges.sort(key = lambda x: x[0])

    return seedNumberRanges[0][0]

print(getLowestLocationNumber(seedNumberRangesPartOne, maps))
print(getLowestLocationNumber(seedNumberRangesPartTwo, maps))
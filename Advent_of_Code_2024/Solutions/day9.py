from Utils.utils import readThisPuzzlesInput
from copy import deepcopy

lines = readThisPuzzlesInput(__file__)

fileSystem = lines[0]
fileStructureOriginal = []

fileId = 0
for i in range(0, len(fileSystem)):
    if i % 2 == 0:
        fileStructureOriginal.append([fileId, int(fileSystem[i])])
        fileId += 1
    else:
        fileStructureOriginal.append([-1, int(fileSystem[i])])

fileStructureOriginal = list(filter(lambda x: x[0] != -1 or x[1] != 0, fileStructureOriginal))

def sumOfFirstNNumbers(n):
    if n <= 0:
        return 0
    return int((n + 1) * n / 2)

def calculateCheckSum(fileStructure):
    index = -1
    sum = 0

    for file in fileStructure:
        index += file[1]

        if file[0] == -1:
            continue

        sum += (sumOfFirstNNumbers(index) - sumOfFirstNNumbers(index - file[1])) * file[0]

    return sum

fileStructure = deepcopy(fileStructureOriginal)

while True:
    firstEmpty = list(filter(lambda x: x[0] == -1, fileStructure))[0].copy()
    lastTaken = list(filter(lambda x: x[0] >= 0, fileStructure))[-1].copy()

    indexOfFirstEmpty = fileStructure.index(firstEmpty)
    indexOfLastTaken = len(fileStructure) - 1 - fileStructure[::-1].index(lastTaken)

    if indexOfFirstEmpty > indexOfLastTaken:
        break

    if firstEmpty[1] > lastTaken[1]:
        fileStructure[indexOfFirstEmpty][1] -= lastTaken[1]
        fileStructure[indexOfLastTaken][0] = -1
        fileStructure.insert(indexOfFirstEmpty, lastTaken)
    elif firstEmpty[1] == lastTaken[1]:
        fileStructure[indexOfFirstEmpty][0] = lastTaken[0]
        fileStructure[indexOfLastTaken][0] = firstEmpty[0]
    else:
        fileStructure[indexOfFirstEmpty][0] = lastTaken[0]
        fileStructure[indexOfLastTaken][1] -= firstEmpty[1]
        fileStructure.insert(indexOfLastTaken + 1, firstEmpty)

print(calculateCheckSum(fileStructure))

fileStructure = deepcopy(fileStructureOriginal)

files = list(filter(lambda x: x[0] >= 0, fileStructure))
files.reverse()
spaces = list(filter(lambda x: x[0] == -1, fileStructure))

for file in files:
    fittingSpaces = list(filter(lambda x : x[0] == -1 and x[1] >= file[1], fileStructure))
    if len(fittingSpaces) == 0:
        continue

    firstFittingSpace = fittingSpaces[0].copy()
    file = file.copy()
    indexOfFittingSpace = fileStructure.index(firstFittingSpace)
    indexOfFile = fileStructure.index(file)

    if indexOfFile < indexOfFittingSpace:
        continue

    if firstFittingSpace[1] > file[1]:
        fileStructure[indexOfFittingSpace][1] -= file[1]
        fileStructure[indexOfFile][0] = -1
        fileStructure.insert(indexOfFittingSpace, file)
    elif firstFittingSpace[1] == file[1]:
        fileStructure[indexOfFittingSpace][0] = file[0]
        fileStructure[indexOfFile][0] = firstFittingSpace[0]

print(calculateCheckSum(fileStructure))
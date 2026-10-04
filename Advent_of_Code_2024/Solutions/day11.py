from Utils.utils import readThisPuzzlesInput
from collections import defaultdict

lines = readThisPuzzlesInput(__file__)

stones = list(map(int, lines[0].split(" ")))

numberOfBlinksPt1 = 25
numberOfBlinksPt2 = 75

def printTotalStones(stonesDict):
    print(sum(stonesDict.values()))

stonesDict = defaultdict(int)

for stone in stones:
    stonesDict[stone] += 1

for i in range(numberOfBlinksPt2):
    newStones = defaultdict(int)

    for stone,count in stonesDict.items():
        if stone == 0:
            newStones[1] += count
            continue
        
        stoneAsStr = str(stone)
        if len(stoneAsStr) % 2 == 0:
            stoneLength = len(stoneAsStr)
            newStones[int(stoneAsStr[: stoneLength // 2])] += count
            newStones[int(stoneAsStr[stoneLength // 2 :])] += count
        else:
            newStones[(stone * 2024)] += count
    
    stonesDict = newStones

    if i+1 in (numberOfBlinksPt1,numberOfBlinksPt2):
        printTotalStones(stonesDict)
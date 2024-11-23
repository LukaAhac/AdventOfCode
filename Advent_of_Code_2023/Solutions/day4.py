from Utils.utils import readThisPuzzlesInput
from collections import defaultdict

lines = readThisPuzzlesInput(__file__)

partOneSum = 0
partTwoSum = 0
scratchcards = defaultdict(int)

for line in lines:
    lineSplit = line.split("|")
    partOneSplit = lineSplit[0].split(":")

    cardNumber = int(partOneSplit[0][5:])
    winningNumbers = set(partOneSplit[1].split())
    scratchedNumbers = set(lineSplit[1].split())

    drawnNumbersCount = len(winningNumbers.intersection(scratchedNumbers))

    if (drawnNumbersCount > 0):
        partOneSum += pow(2, drawnNumbersCount - 1)

    scratchcards[cardNumber] += 1

    for i in range(1, drawnNumbersCount + 1):
        scratchcards[cardNumber + i] += scratchcards[cardNumber]

partTwoSum = sum(scratchcards.values())

print(partOneSum)
print(partTwoSum)
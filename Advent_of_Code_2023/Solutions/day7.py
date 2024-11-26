from Utils.utils import readThisPuzzlesInput
from functools import cmp_to_key

lines = readThisPuzzlesInput(__file__)

handsAndBids = []

for line in lines:
    lineSplit = line.split()
    handsAndBids.append((lineSplit[0], int(lineSplit[1])))

cardToStrengthMapPartOne = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}
cardToStrengthMapPartTwo = cardToStrengthMapPartOne.copy()
cardToStrengthMapPartTwo['J'] = 1

def getHandShape(hand, part):
    cards = list(hand)
    uniqueCards = set(cards)

    numberOfSameCards = []
    numberOfJokers = 0

    for card in uniqueCards:
        if card == 'J' and part == 2:
            numberOfJokers = cards.count(card)
        else:
            numberOfSameCards.append(cards.count(card))

    numberOfSameCards.sort(reverse = True)
    if (numberOfJokers > 0):
        numberOfSameCards.append(str(numberOfJokers) + 'J')

    return numberOfSameCards

def getHandStrength(hand, part):
    handShape = getHandShape(hand, part)

    match handShape:
        case [5] | ['5J'] | [1, '4J'] | [2, '3J'] | [3, '2J'] | [4, '1J']:
            return 7
        case [4,1] | [3, 1, '1J'] | [2, 1, '2J'] | [1, 1, '3J']:
            return 6
        case [3,2] | [2, 2, '1J']:
            return 5
        case [3,1,1] | [2, 1, 1, '1J'] | [1, 1, 1, '2J']:
            return 4
        case [2,2,1]:
            return 3
        case [2,1,1,1] | [1, 1, 1, 1, '1J']:
            return 2
        case [1,1,1,1,1]:
            return 1

def compareHands(handAndBidOne, handAndBidTwo, part):
    handOne = handAndBidOne[0]
    handTwo = handAndBidTwo[0]

    handOneSrength = getHandStrength(handOne, part)
    handTwoStrength = getHandStrength(handTwo, part)

    if (handOneSrength != handTwoStrength):
        return handOneSrength - handTwoStrength
    
    if part == 1:
        cardsToStrengthMap = cardToStrengthMapPartOne
    else:
        cardsToStrengthMap = cardToStrengthMapPartTwo

    for i in range(0, len(handOne)):
        if handOne[i] != handTwo[i]:
            return cardsToStrengthMap[handOne[i]] - cardsToStrengthMap[handTwo[i]]
    return 0

def compareHandsPartOne(handAndBidOne, handAndBidTwo):
    return compareHands(handAndBidOne, handAndBidTwo, 1)

def compareHandsPartTwo(handAndBidOne, handAndBidTwo):
    return compareHands(handAndBidOne, handAndBidTwo, 2)

def calcualteSum(handsAndBids):
    totalSum = 0
    for i in range(0, len(handsAndBids)):
        totalSum += handsAndBids[i][1] * (i + 1)
    return totalSum

handsAndBids = sorted(handsAndBids, key = cmp_to_key(compareHandsPartOne))
print(calcualteSum(handsAndBids))
handsAndBids = sorted(handsAndBids, key = cmp_to_key(compareHandsPartTwo))
print(calcualteSum(handsAndBids))
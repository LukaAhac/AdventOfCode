from Utils.utils import readThisPuzzlesInput
import math
from functools import cmp_to_key

lines = readThisPuzzlesInput(__file__)

rules = []
updates = []

isRuleLine = True
for line in lines:
    if line == "":
        isRuleLine = False
        continue

    if isRuleLine:
        first,second = map(int, line.split("|"))
        rules.append((first, second))
    else:
        updates.append(list(map(int, line.split(","))))

def getTargetRules(page):
    targetRules = []
    for rule in rules:
        if rule[1] == page:
            targetRules.append(rule)

    return targetRules

def getMiddlePage(page):
    return page[math.floor(len(page) / 2)]

partOneSum = 0
partTwoSum = 0
incorrectlyOrderdUpdates = []

for page in updates:
    pageIsValid = True
    for i in range(0, len(page)):
        targetRules = getTargetRules(page[i])
        for rule in targetRules:
            if page.count(rule[0]) > 0 and page.index(rule[0]) > i:
                pageIsValid = False
                break
    if pageIsValid:
        partOneSum += getMiddlePage(page)
    else:
        incorrectlyOrderdUpdates.append(page)

def comparePagesAccordingToRules(a, b):
    if rules.count((a, b)) > 0:
        return -1
    elif rules.count((b, a)) > 0:
        return 1
    else:
        return 0

for page in incorrectlyOrderdUpdates:
    page = sorted(page, key = cmp_to_key(comparePagesAccordingToRules))
    partTwoSum += getMiddlePage(page)

print(partOneSum)
print(partTwoSum)
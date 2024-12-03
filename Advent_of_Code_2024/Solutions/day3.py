from Utils.utils import readThisPuzzlesInput
import re

lines = readThisPuzzlesInput(__file__)

code = str.join("", lines)

partOneSum = 0
partTwoSum = 0

def calculateMul(mul):
    a,b = mul[4:-1].split(",")
    return int(a) * int(b)

muls = re.findall(r"mul\([0-9]+,[0-9]+\)", code)

for mul in muls:
    partOneSum += calculateMul(mul)

splitPerDo = re.split(r"do\(\)", code)

for split in splitPerDo:
    splitPerDont = re.split(r"don't\(\)", split)
    doMuls = splitPerDont[0]
    mulsInDo = re.findall(r"mul\([0-9]+,[0-9]+\)", doMuls)
    for mul in mulsInDo:
        partTwoSum += calculateMul(mul)

print(partOneSum)
print(partTwoSum)
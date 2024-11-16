from Utils.utils import readThisPuzzlesInput

lines = readThisPuzzlesInput(__file__)

def lineStartsWithNumber(line):
    for number in numbersMapping:
        if line.startswith(number):
            return numbersMapping[number]
    return -1

def lineEndsWithNumber(line):
    for number in numbersMapping:
        if line.endswith(number):
            return numbersMapping[number]
    return -1

partOneSum = 0
partTwoSum = 0

numbersMapping = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

for line in lines:
    firstNum = 0
    lastNum = 0
    for char in line:
        if char.isdigit():
            firstNum = int(char)
            break
    for char in line[::-1]:
        if char.isdigit():
            lastNum = int(char)
            break
    
    partOneSum += firstNum * 10 + lastNum

for line in lines:
    firstNum = 0
    lastNum = 0
    for index in range(0, len(line)):
        char = line[index]
        if char.isdigit():
            firstNum = int(char)
            break
        value = lineStartsWithNumber(line[index:])
        if value != -1:
            firstNum = value
            break
    for index in range(len(line) - 1, -1, -1):
        char = line[index]
        if char.isdigit():
            lastNum = int(char)
            break
        value = lineEndsWithNumber(line[:index + 1])
        if value != -1:
            lastNum = value
            break
    
    partTwoSum += firstNum * 10 + lastNum

print(partOneSum)
print(partTwoSum)
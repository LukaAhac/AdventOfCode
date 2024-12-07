from Utils.utils import readThisPuzzlesInput
from itertools import product

lines = readThisPuzzlesInput(__file__)

def calculate(a, b, operator):
    if operator == '*':
        return a * b
    elif operator == '+':
        return a + b
    elif operator == "||":
        return int(str(a) + str(b))
    
def hasValidArrangement(result, numbers, operatorArrangements):
    for arrangement in operatorArrangements:
        tempResult = 0
        for i in range(0, operatorsCount):
            if i == 0:
                tempResult = calculate(numbers[i], numbers[i + 1], arrangement[i])
            else:
                tempResult = calculate(tempResult, numbers[i + 1], arrangement[i])

            if tempResult > result:
                break
        
        if result == tempResult:
            return True
        
    return False
    
partOneSum = 0
partTwoSum = 0

for line in lines:
    result,numbers = line.split(":")
    result = int(result)
    numbers = list(map(int, numbers.strip().split(" ")))

    operatorsCount = len(numbers) - 1
    operatorArrangementsPartOne = list(product(["*", "+"], repeat = operatorsCount))
    operatorArrangementsPartTwo = list(product(["*", "+", "||"], repeat = operatorsCount))

    if hasValidArrangement(result, numbers, operatorArrangementsPartOne):
        partOneSum += result
    if hasValidArrangement(result, numbers, operatorArrangementsPartTwo):
        partTwoSum += result

print(partOneSum)
print(partTwoSum)
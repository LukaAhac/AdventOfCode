from Utils.utils import readThisPuzzlesInput

lines = readThisPuzzlesInput(__file__)

partOneSum = 0
partTwoSum = 0

availableCubes = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}

for line in lines:
    gameImpossible = False
    lineSplit = line.split(":")
    gameId = int(lineSplit[0][5:])
    draws = lineSplit[1].split(";")

    colorToAmount = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }

    for draw in draws:
        colorSeparatedCubes = draw.strip().split(",")
        for cubes in colorSeparatedCubes:
            (amount, color) = cubes.strip().split(" ")

            amount = int(amount)

            if amount > availableCubes[color]:
                gameImpossible = True

            if colorToAmount[color] < amount:
                colorToAmount[color] = amount

    if not gameImpossible:
        partOneSum += gameId

    value = 1
    for colorAmount in colorToAmount.values():
        value *= colorAmount

    partTwoSum += value

print(partOneSum)
print(partTwoSum)
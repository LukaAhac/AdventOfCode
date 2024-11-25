from Utils.utils import readThisPuzzlesInput
import math

lines = readThisPuzzlesInput(__file__)

times = [int(x) for x in lines[0].split(":")[1].split()]
distances = [int(x) for x in lines[1].split(":")[1].split()]

def solve(times, distances):
    multiple = 1
    for i in range(0, len(times)):
        time = times[i]
        distance = distances[i]

        discriminant = math.sqrt(math.pow(time, 2) - 4 * distance)
        t1 = math.floor((time - discriminant) / 2)
        t2 = math.ceil((time + discriminant) / 2)
        multiple *= t2 - t1 -1

    return multiple

partTwoTime = int("".join([str(x) for x in times]))
partTwoDistance = int("".join([str(x) for x in distances]))

print(solve(times, distances))
print(solve([partTwoTime], [partTwoDistance]))
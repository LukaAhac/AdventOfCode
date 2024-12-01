from Utils.utils import readThisPuzzlesInput

lines = readThisPuzzlesInput(__file__)

list1 = []
list2 = []

for line in lines:
    lineSplit = line.split()
    list1.append(int(lineSplit[0]))
    list2.append(int(lineSplit[1]))

partOneSum = 0
partTwoSum = 0

list1.sort()
list2.sort()

for i in range(0, len(list1)):
    partOneSum += abs(list1[i] - list2[i])

print(partOneSum)

for number in list1:
    partTwoSum += list2.count(number) * number

print(partTwoSum)
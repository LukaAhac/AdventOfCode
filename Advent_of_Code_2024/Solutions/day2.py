from Utils.utils import readThisPuzzlesInput

lines = readThisPuzzlesInput(__file__)

reports = []

for line in lines:
    reports.append([int(x) for x in line.split()])

partOneSum = 0
partTwoSum = 0

def isReportValid(report):
    if not (report == sorted(report) or report == sorted(report, reverse=True)):
        return False
    
    for i in range(0, len(report) - 1):
        subtraction = report[i] - report[i + 1]
        if not 1 <= abs(subtraction) <= 3:
            return False
        
    return True

for report in reports:
    if isReportValid(report):
        partOneSum += 1
        partTwoSum += 1
    else:
        for i in range(0, len(report)):
            if isReportValid(report[:i] + report[i + 1 :]):
                partTwoSum += 1
                break

print(partOneSum)
print(partTwoSum)
# Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

# After 256 days in the example above, there would be a total of 26984457539 lanternfish!

# How many lanternfish would there be after 256 days

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day6-Lanternfish\input.txt") as f:
    data = f.readlines()

#Given input
inp = []

#Parse input
for line in data:
    line = line.strip()
    inp.append(line)

#We have onlny one row
inp = inp[0].split(",")
#Max timer is 8 when fish is created
max_timer = 8
#Number of fays
daysNum = 256

#Dict of fishes where key is the number of days until creation of a new one
fishes = dict()

#Create a key for each timer
for timer in range(max_timer+1):
    fishes[str(timer)] = 0

#Mark each fish in the dictionary
for fish in inp:

    fishes[fish] += 1

#Go through the fishes in ascending order
keys = sorted(fishes.keys())

for index in range(daysNum):

    #Number of fishes that will be created
    newFish = fishes["0"]

    for key in keys:

        #If it is not number of fishes with the timer 0
        if key != "0":
            #Add their number to the that timer - 1
            fishes[str(int(key)-1)] += fishes[key]
        #Put their number to zero
        fishes[key] = 0

    #Each fish that creates new one, goes back to timer of 6
    fishes["6"] += newFish
    #Each fish that has been just created goes to timer of 8
    fishes["8"] += newFish

#Variable to count the fishes
counter = 0

#Count all the fishes
for fish in fishes:

    counter += fishes[fish]

print("There would be {} lanternfish after {} days".format(counter,daysNum))
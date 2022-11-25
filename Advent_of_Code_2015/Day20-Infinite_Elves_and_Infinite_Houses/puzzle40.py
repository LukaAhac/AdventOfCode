# The Elves decide they don't want to visit an infinite number of houses. Instead, each Elf will stop after delivering presents to 50 houses. 
# To make up for it, they decide to deliver presents equal to eleven times their number at each house.

# With these changes, what is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Input data
data = 36000000
#Let's assume house number is less than a milion, assumption was right - othervise i would look from houses number 1 milion to 2 milion etc...
houses = [0]*1000000

#For each elf 1,2,3...
for index1 in range(1,len(houses)):

    #Start with elf number
    index2 = index1
    #Variable to count number of deliveries
    delivered = 0

    #While we dont reach all milion houses
    while True:
        #If we updated all milion houses break
        if index2 >= 1000000 or delivered >= 50:
            break
        #Add elf gifts to the house
        houses[index2] += index1*11
        #Increase index by elf number
        index2 += index1
        #Increase number of deliveries by one
        delivered += 1

#Look if we found solution
for index in range(len(houses)):
    if houses[index] >= data:
        print(index,"is the number of the house")
        exit()
print("Not found")
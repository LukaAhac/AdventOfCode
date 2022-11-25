# Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

# You have 500 Aunts named "Sue".

# So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. 
# You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

# The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those 
# compounds there are. According to the instructions, these are what the MFCSAM can detect:

# children, by human DNA age analysis.
# cats. It doesn't differentiate individual breeds.
# Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
# goldfish. No other kinds of fish.
# trees, all in one group.
# cars, presumably by exhaust or gasoline or something.
# perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
# In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times
# and then prints out a message on ticker tape:

# children: 3
# cats: 7
# samoyeds: 2
# pomeranians: 3
# akitas: 0
# vizslas: 0
# goldfish: 5
# trees: 3
# cars: 2
# perfumes: 1
# You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

# What is the number of the Sue that got you the gift?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day16-Aunt_Sue\input.txt") as f:
    data = f.readlines()
#Outpot given by My First Crime Scene Analysis Machine
MFCSAM_output = {"children":3,"cats":7,"samoyeds":2,"pomeranians":3,"akitas":0,"vizslas":0,"goldfish":5,"trees":3,"cars":2,"perfumes":1}
#List of possible auints -> expecting to be only one but still making a list
possible_aunt = []

#For each aunt
for aunt in data:
    aunt = aunt.strip().split()
    #Set the possiblity flag to true
    auntFlag = True

    #Check if properties are equal to those generated by MFCSAM, if not set flag to false
    for index in range(1,int(len(aunt)/2)):
        #Last property in the input does not have a comma, so watch out on that
        if index == int(len(aunt)/2)-1:
            if MFCSAM_output[aunt[index*2][:-1]] != int(aunt[index*2+1]):
                auntFlag = False
        else:
            if MFCSAM_output[aunt[index*2][:-1]] != int(aunt[index*2+1][:-1]):
                auntFlag = False
    #If flag is true, then add aunt number to the list
    if auntFlag:
        possible_aunt.append(int(aunt[1][:-1]))   

print("The number of the Sue that sent the gift is",possible_aunt)
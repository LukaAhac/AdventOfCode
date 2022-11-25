# The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run 
# more steps of the pair insertion process; a total of 40 steps should do it.

# In the above example, the most common element is B (occurring 2192039569602 times) and the least 
# common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.

# Apply 40 steps of pair insertion to the polymer template and find the most and least common elements 
# in the result. What do you get if you take the quantity of the most common element and 
# subtract the quantity of the least common element?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day14-Extended_Polymerization\input.txt") as f:
    data = f.readlines()

#Given input
inp = []
steps = 40

#Parse input
for line in data:
    line = line.strip()
    inp.append(line)

#Polymer in the first line
poly = inp[0]
#Chemical reactions from line 2 up to the end
inp = inp[2:]

#Parse reaction instructions
ins = dict()

for i in inp:

    i = i.split()

    ins[i[0]] = i[2]

#Mark each adjacent letters
#NOTE: by marking it this way we are marking each of letters,beside first and list, TWICE
#So we additionaly need to trak first and last aswell, and devide by 2 at the end
adjacent = dict()

for ind in range(1,len(poly)):

    if poly[ind-1:ind+1] not in adjacent:
        adjacent[poly[ind-1:ind+1]] = 1
    else:
        adjacent[poly[ind-1:ind+1]] += 1

first = poly[:2]
last = poly[-2:]

#Current adjacents
curr = adjacent

#Do the magic
for _ in range(steps):

    #Dictionary for new adjacents
    newAdj = dict()

    #For current adjacent, produce the new ones according to the rules
    for a in curr:

        #Keep track if we cahge first/last
        if a == first:
            first = a[0]+ins[a]

        if a == last:
            last = ins[a]+a[1]

        #Add new ones
        new = [a[0]+ins[a],ins[a]+a[1]]

        for x in new:

            if x in newAdj:
                newAdj[x] += curr[a]
            else:
                newAdj[x] = curr[a]

    #New is now current
    curr = newAdj

#Count the letters
counter = dict()

for c in curr:

    elems = [c[0],c[1]]

    for x in elems:

        if x in counter:
            counter[x] += curr[c]

        else:
            counter[x] = curr[c]

#Since we counted each twice beside first and last, add them
counter[first[0]] += 1
counter[last[1]] += 1

#Devide everything by 2 so we have real values
values = list(counter.values())
values = list(map(lambda x: x//2,values))

#Output
print("If I take the quantity of the most common element and subtract the quantity of the least common element I get :",max(values)-min(values))
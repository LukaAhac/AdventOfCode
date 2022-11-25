# The incredible pressures at this depth are starting to put a strain on your submarine. The submarine 
# has polymerization equipment that would produce suitable materials to reinforce the submarine, and 
# the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.

# The submarine manual contains instructions for finding the optimal polymer formula; specifically, 
# it offers a polymer template and a list of pair insertion rules (your puzzle input). You just need
#  to work out what polymer would result after repeating the pair insertion process a few times.

# For example:

# NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C
# The first line is the polymer template - this is the starting point of the process.

# The following section defines the pair insertion rules. A rule like AB -> C means that when 
# elements A and B are immediately adjacent, element C should be inserted between them. 
# These insertions all happen simultaneously.

# So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

# The first pair (NN) matches the rule NN -> C, so element C is inserted between the 
# first N and the second N.
# The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
# The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.
# Note that these pairs overlap: the second element of one pair is the first element of the next pair. 
# Also, because all pairs are considered simultaneously, inserted elements are not considered to be 
# part of a pair until the next step.

# After the first step of this process, the polymer becomes NCNBCHB.

# Here are the results of a few steps using the above rules:

# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB
# After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
# After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
# This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. 
# After step 10, B occurs 1749 times, C occurs 298 times, H occurs 191 times, and N occurs 865 times; 
# taking the quantity of the most common element (B, 1749) and subtracting the quantity of the least 
# common element (H, 161) produces 1749 - 161 = 1588.

# Apply 10 steps of pair insertion to the polymer template and find the most and least common elements 
# in the result. What do you get if you take the quantity of the most common element and subtract the 
# quantity of the least common element?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day14-Extended_Polymerization\input.txt") as f:
    data = f.readlines()

#Given input
inp = []
steps = 10

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
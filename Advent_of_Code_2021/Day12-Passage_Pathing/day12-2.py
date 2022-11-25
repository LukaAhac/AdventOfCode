# After reviewing the available paths, you realize you might have time to visit a single small cave twice. 
# Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, 
# and the remaining small caves can be visited at most once. However, the caves named start and end can only 
# be visited exactly once each: once you leave the start cave, you may not return to it, and once you reach 
# the end cave, the path must end immediately.

# Now, the 36 possible paths through the first example above are:

# start,A,b,A,b,A,c,A,end
# start,A,b,A,b,A,end
# start,A,b,A,b,end
# start,A,b,A,c,A,b,A,end
# start,A,b,A,c,A,b,end
# start,A,b,A,c,A,c,A,end
# start,A,b,A,c,A,end
# start,A,b,A,end
# start,A,b,d,b,A,c,A,end
# start,A,b,d,b,A,end
# start,A,b,d,b,end
# start,A,b,end
# start,A,c,A,b,A,b,A,end
# start,A,c,A,b,A,b,end
# start,A,c,A,b,A,c,A,end
# start,A,c,A,b,A,end
# start,A,c,A,b,d,b,A,end
# start,A,c,A,b,d,b,end
# start,A,c,A,b,end
# start,A,c,A,c,A,b,A,end
# start,A,c,A,c,A,b,end
# start,A,c,A,c,A,end
# start,A,c,A,end
# start,A,end
# start,b,A,b,A,c,A,end
# start,b,A,b,A,end
# start,b,A,b,end
# start,b,A,c,A,b,A,end
# start,b,A,c,A,b,end
# start,b,A,c,A,c,A,end
# start,b,A,c,A,end
# start,b,A,end
# start,b,d,b,A,c,A,end
# start,b,d,b,A,end
# start,b,d,b,end
# start,b,end
# The slightly larger example above now has 103 paths through it, and the even larger example 
# now has 3509 paths through it.

# Given these new rules, how many paths through this cave system are there?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day12-Passage_Pathing\input.txt") as f:
    data = f.readlines()

#Given input
inp = []

#Parse input
for line in data:
    line = line.strip().split("-")
    inp.append(line)

#Dictionary of moves from each location
toGo = dict()

#Make the move dict
for line in inp:

    if line[0] not in toGo:
        toGo[line[0]] = [line[1]]

    else:
        toGo[line[0]].append(line[1])

    if line[1] not in toGo:
        toGo[line[1]] = [line[0]]

    else:
        toGo[line[1]].append(line[0])


#Initiall path is start, and all paths will have a flag to track wheter or not they already
#visited one small cave
paths = [(["start"],False)]
#All ended paths
ended = []

#While there are paths that are not ended
while len(paths) > 0:

    #List for next iteration
    nextPaths = []

    #For each path
    for p,flag in paths:

        #If it reached end, put him into the ended list
        if p[-1] == "end":
            ended.append(p)
            continue

        #Else construct possible moves from last spot
        moveList = toGo[p[-1]]
        possibleMoves = []
        #Second move to the samll case goes to this list
        doubleMoves = []

        #We can go to the small cave only once, and not to start or end
        for m in moveList:

            if m in p and m.islower() and flag is True:
                continue
            elif m in p and m in ("start","end"):
                continue
            elif m.islower() and m not in p:
                possibleMoves.append(m)
            elif m.islower() and m in p and flag is False:
                doubleMoves.append(m)
            else:
                possibleMoves.append(m)
            
        #If there are no moves, go to the next path
        if len(possibleMoves) == 0 and len(doubleMoves) == 0:
            continue

        #For possible moves consturt the move with copied flag
        for move in possibleMoves:
            newP = p.copy()
            newP.append(move)
            nextPaths.append((newP,flag))
        #For the moves to the small cave second time, construct the moves with flag = True
        for move in doubleMoves:
            newP = p.copy()
            newP.append(move)
            nextPaths.append((newP,True))

    #Set paths for next iteratoon
    paths = nextPaths

#Output
print("Given these new rules, there are {} paths through this cave system.".format(len(ended)))
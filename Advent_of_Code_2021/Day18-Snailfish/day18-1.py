# You descend into the ocean trench and encounter some snailfish. They say they saw the sleigh keys! They'll even tell 
# you which direction the keys went if you help one of the smaller snailfish with his math homework.

# Snailfish numbers aren't like regular numbers. Instead, every snailfish number is a pair - an ordered list of two 
# elements. Each element of the pair can be either a regular number or another pair.

# Pairs are written as [x,y], where x and y are the elements within the pair. Here are some example snailfish numbers, 
# one snailfish number per line:

# [1,2]
# [[1,2],3]
# [9,[8,7]]
# [[1,9],[8,5]]
# [[[[1,2],[3,4]],[[5,6],[7,8]]],9]
# [[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
# [[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
# This snailfish homework is about addition. To add two snailfish numbers, form a pair from the left and right parameters 
# of the addition operator. For example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]].

# There's only one problem: snailfish numbers must always be reduced, and the process of adding two snailfish numbers 
# can result in snailfish numbers that need to be reduced.

# To reduce a snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:

# If any pair is nested inside four pairs, the leftmost such pair explodes.
# If any regular number is 10 or greater, the leftmost such regular number splits.
# Once no action in the above list applies, the snailfish number is reduced.

# During reduction, at most one action applies, after which the process returns to the top of the list of actions. 
# For example, if split produces a pair that meets the explode criteria, that pair explodes before other splits occur.

# To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), 
# and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding 
# pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number 0.

# Here are some examples of a single explode action:

# [[[[[9,8],1],2],3],4] becomes [[[[0,9],2],3],4] (the 9 has no regular number to its left, so it is not added to any 
# regular number).
# [7,[6,[5,[4,[3,2]]]]] becomes [7,[6,[5,[7,0]]]] (the 2 has no regular number to its right, and so it is not added to any 
# regular number).
# [[6,[5,[4,[3,2]]]],1] becomes [[6,[5,[7,0]]],3].
# [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] (the pair [3,2] is unaffected because the 
# pair [7,3] is further to the left; [3,2] would explode on the next action).
# [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[7,0]]]].
# To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided by 
# two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up. 
# For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on.

# Here is the process of finding the reduced result of [[[[4,3],4],4],[7,[[8,4],9]]] + [1,1]:

# after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
# after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
# after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
# after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
# after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
# after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
# Once no reduce actions apply, the snailfish number that remains is the actual result of the 
# addition operation: [[[[0,7],4],[[7,8],[6,0]]],[8,1]].

# The homework assignment involves adding up a list of snailfish numbers (your puzzle input). The snailfish numbers are 
# each listed on a separate line. Add the first snailfish number and the second, then add that result and the third, 
# then add that result and the fourth, and so on until all numbers in the list have been used once.

# For example, the final sum of this list is [[[[1,1],[2,2]],[3,3]],[4,4]]:

# [1,1]
# [2,2]
# [3,3]
# [4,4]
# The final sum of this list is [[[[3,0],[5,3]],[4,4]],[5,5]]:

# [1,1]
# [2,2]
# [3,3]
# [4,4]
# [5,5]
# The final sum of this list is [[[[5,0],[7,4]],[5,5]],[6,6]]:

# [1,1]
# [2,2]
# [3,3]
# [4,4]
# [5,5]
# [6,6]
# Here's a slightly larger example:

# [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
# [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
# [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
# [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
# [7,[5,[[3,8],[1,4]]]]
# [[2,[2,2]],[8,[8,1]]]
# [2,9]
# [1,[[[9,3],9],[[9,0],[0,7]]]]
# [[[5,[7,4]],7],1]
# [[[[4,2],2],6],[8,7]]
# The final sum [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] is found after adding up the above snailfish numbers:

#   [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
# + [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
# = [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]

#   [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
# + [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
# = [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]

#   [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
# + [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
# = [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]

#   [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
# + [7,[5,[[3,8],[1,4]]]]
# = [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]

#   [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
# + [[2,[2,2]],[8,[8,1]]]
# = [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]

#   [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
# + [2,9]
# = [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]

#   [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
# + [1,[[[9,3],9],[[9,0],[0,7]]]]
# = [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]

#   [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
# + [[[5,[7,4]],7],1]
# = [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]

#   [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
# + [[[[4,2],2],6],[8,7]]
# = [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
# To check whether it's the right answer, the snailfish teacher only checks the magnitude of the final sum. 
# The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its 
# right element. The magnitude of a regular number is just that number.

# For example, the magnitude of [9,1] is 3*9 + 2*1 = 29; the magnitude of [1,9] is 3*1 + 2*9 = 21. 
# Magnitude calculations are recursive: the magnitude of [[9,1],[1,9]] is 3*29 + 2*21 = 129.

# Here are a few more magnitude examples:

# [[1,2],[[3,4],5]] becomes 143.
# [[[[0,7],4],[[7,8],[6,0]]],[8,1]] becomes 1384.
# [[[[1,1],[2,2]],[3,3]],[4,4]] becomes 445.
# [[[[3,0],[5,3]],[4,4]],[5,5]] becomes 791.
# [[[[5,0],[7,4]],[5,5]],[6,6]] becomes 1137.
# [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] becomes 3488.
# So, given this example homework assignment:

# [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# [[[5,[2,8]],4],[5,[[9,9],0]]]
# [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# [[[[5,4],[7,7]],8],[[8,3],8]]
# [[9,3],[[9,9],[6,[4,9]]]]
# [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
# The final sum is:

# [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
# The magnitude of this final sum is 4140.

# Add up all of the snailfish numbers from the homework assignment in the order they appear. 
# What is the magnitude of the final sum?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day18-Snailfish\input.txt") as f:
    data = f.readlines()
    
#Given input
inp = []

#Parse input
for line in data:
    line = line.strip()
    inp.append(line)

#Take first as current and remove it from the list
current = inp[0]
inp = inp[1:]

#For each snail number add it with current one and reduce the result
for sn in inp:

    #Addition
    current = "[" + current + "," + sn + "]"

    #Reduction
    #Flag to indicate when there is no more to reduce
    actionPerformed = True

    #Perfrom reduction until there is no more to reduce
    while actionPerformed:

        #Initially set the flag to False, if we perfomred the reduciton we will set it
        #to True so loop will enter another iteration
        actionPerformed = False

        depth = 0
        startIndex = None

        #Check whether one of pair reaches depth 5 and will explode
        #If there are any, get its starting index - we stop at the first found
        for index in range(len(current)):

            if current[index] == "[":
                depth += 1
            elif current[index] == "]":
                depth -= 1

            if depth == 5:
                startIndex = index
                break

        #If there is a pair at depth 5 explode it
        if depth == 5:

            #Indicate that we are perfomring the acitoon in this interatin
            actionPerformed = True

            toExplode = ""
            endIndex = startIndex

            #Start index is at "[" of the pair that will explode, calculate the 
            #index of the "]" for coresponding pair
            #Also copy that pari into toExplode string
            while current[endIndex] != "]":

                toExplode += current[endIndex]
                endIndex += 1

            #We did not add the final "]" in the loop, so add it now
            toExplode += "]"
            #Increase endIndex so it shows at the first character after exploded pair
            endIndex += 1
  
            #Get the number in the pair
            x,y = list(map(int,current[startIndex:endIndex][1:-1].split(",")))


            leftStart = None
            leftEnd = None

            index = startIndex

            #Look for the closest left number of the pair that will explode
            #Do that by checking characters starting from exploding pair going to begining
            while index > 0:

                index -= 1

                #If the character is not one of "[","]" or "," then it must be a number
                #And remember its endIndex - end because we are going from right to left
                #Increase it by 1 so the end index points behind the number
                if current[index] not in {"[",",","]"} and leftEnd is None:
                    leftEnd = index+1

                #If we found a number, find its left index aswell amd then break out of the loop
                #Increase it by 1 so it points to the first position of the number
                #Now start index will point to the first character of the number
                #And the end index will point behinf the number
                if leftEnd is not None and current[index] in {"[",",","]"}:
                    leftStart = index+1
                    break
            
            #If we found a number then add him the x value of the exploding pair
            if leftStart is not None and leftEnd is not None:

                leftNumber = int(current[leftStart:leftEnd])
                leftNumber += x


            rightStart = None
            rightEnd = None

            #Look for the closest right number
            #Start looking from behinde the pair all the way to the right
            for index in range(endIndex,len(current)):

                #If the character is not one of "[","]" or "," then it must be a number
                #Remember its start index
                if current[index] not in {"[",",","]"} and rightStart is None:
                    rightStart = index

                #If we found a start index, check for the first char that is not a number
                #Remember its end index
                #Start index now points to the first char of a number, while end index points
                #to behind number
                if rightStart is not None and current[index] in {"[",",","]"}:
                    rightEnd = index
                    break
                
                index += 1

            #If we found the number to the right, then add him the y value
            if rightStart is not None and rightEnd is not None:

                rightNumber = int(current[rightStart:rightEnd])
                rightNumber += y


            #Construct the new exploded number
            exploded = ""

            #If there is a number to the left of exploding pair
            #Copy everything up to that number
            #Replace the number with newly calcualted one
            #Copy everythin from the right of the number up to the exploding pair
            if leftStart is not None and leftEnd is not None:

                exploded += current[:leftStart]
                exploded += str(leftNumber)
                exploded += current[leftEnd:startIndex]
            #If there is no number on the left, copy everything up to the exploding pair
            else:
                exploded += current[:startIndex]

            #Replace the exploding pair with the zero
            exploded += "0"

            #If there is a number to the right of exploding pair
            #Copy everything between exploading pair and the number
            #Replace the number with newly calculated one
            #Copy everyting from the number up to the end
            if rightStart is not None and rightEnd is not None:

                exploded += current[endIndex:rightStart]
                exploded += str(rightNumber)
                exploded += current[rightEnd:]
            #If there is no number on the right, copy everything up to the end
            else:
                exploded += current[endIndex:]

            #Updathe the current and start the loop again
            current = exploded
            continue


        #If there is nothing to explode, check if there is something to split
        startIndex = None
        endIndex = None
        inNumber = False

        #Go through the string and check wheter it contains the number that is 
        #larger or equal to the 10, if there is such number, remeber its starting
        #and ending index
        for index in range(len(current)):

            #If we find the char that is not on of "[","]" or "," then in must be a number
            if current[index] not in {"[",",","]"} and inNumber is False:
                inNumber = True
                startIndex = index

            #Once we found the number scan until the end of it
            #Start index will point to the first position of a number, while end index
            #will point behinf the number
            elif current[index] in {"[",",","]"} and inNumber is True:
                inNumber = False
                endIndex = index

                #Convert him to the int
                number = int(current[startIndex:endIndex])

                #Compare it to 10 and set the flag if it is larger or equal
                if number >= 10:
                    actionPerformed = True
                    break

        #Split the number if needed
        if actionPerformed:

            #Devide it by two and round down
            x = number//2
            #Devide it by two and round up
            y = (number+1)//2

            #Construct the new pair
            new = "[" + str(x) + "," + str(y) + "]"
            
            #Inset the new pair insted of a number
            splitted = current[:startIndex]
            splitted += new
            splitted += current[endIndex:]

            #Updathe the current and loop agian
            current = splitted
            continue

#Calculate the magnitued
calcPerformed = True

#Loop until there is no more calculatiosn to do
while calcPerformed:

    #Indicate that there is no calculation done so far
    calcPerformed = False

    leftIndex = None
    rightIndex = None

    #Loop through the string and find the first pair that has been closed
    #The first pair thaw has been closed with "]" will always be [x,y] pair
    #Find the start and end index of the pair
    for index in range(len(current)):

        if current[index] == "[":
            #Increment by 1 so it will point to the number
            leftIndex = index + 1
        if current[index] == "]":
            rightIndex = index
            break

    if rightIndex is not None:

        x,y = list(map(int,current[leftIndex:rightIndex].split(",")))

        #Calculate the new value
        new = 3*x+2*y

        #Replace the pair with newly calculated value
        calculated = ""
        calculated += current[:leftIndex-1]
        calculated += str(new)
        calculated += current[rightIndex+1:]
        calcPerformed = True

    #Update current
    current = calculated

#Output
print("The magnitude of the final sum is :",current)
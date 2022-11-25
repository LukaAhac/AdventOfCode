# You notice a second question on the back of the homework assignment:

# What is the largest magnitude you can get from adding only two of the snailfish numbers?

# Note that snailfish addition is not commutative - that is, x + y and y + x can produce 
# different results.

# Again considering the last example homework assignment above:

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
# The largest magnitude of the sum of any two snailfish numbers in this list is 3993. 
# This is the magnitude of [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]] + [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]], 
# which reduces to [[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]].

# What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?

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

#List of magnitudes
magnitudes = []

#For each pair of numbers that are not the same calculate their sum
#And put the result magniuted in the list
for index1 in range(len(inp)):

    for index2 in range(len(inp)):

        if index1 == index2:
            continue

        current = "[" + inp[index1] + "," + inp[index2] + "]"

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
        
        #Add magnitued to the list
        magnitudes.append(int(current))

#Output
print("The largest magnitude of any sum of two different snailfish numbers from the homework assignment is :",max(magnitudes))
# Uh oh - the Accounting-Elves have realized that they double-counted everything red.

# Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

# [1,2,3] still has a sum of 6.
# [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
# {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
# [1,"red",5] has a sum of 6, because "red" in an array has no effect.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day12-JSAbacusFramework.io\input.txt") as f:
    data = f.readlines()

#Input is one line
data = data[0]
#Number as a string
number = ""
#Object level
level = 0
#Dictionary that saves number ber object level
number_per_level = dict()
#Initialize level 0 to empty list
number_per_level[0] = []
#Dictionary that trackes if "red" is found in the current level
red_in_level = dict()
#Initialize level 0 to False
red_in_level[0] = False
#Tracks wheter we are in object or list by checking which parentheses, { or [, is last
parentheses = []

#For each character in data
for index in range(len(data)):

    #If the character is opening parenthesis, note that into the parentheses variable
    if data[index] == "{" or data[index] == "[":
        parentheses.append(data[index])
    #If the character is closing parenthesis, remove last parenthesis from the parenthesis variable
    elif data[index] == "]" or data[index] == "}":
        parentheses.pop()

    #If the charachter is "{"
    if data[index] == "{":
        #If the number is found save it to the current level
        if len(number) > 0:
            number_per_level[level].append(int(number))
            number = ""
        #Open new level
        level += 1
        #Open list for level numbers
        number_per_level[level] = []
        #Set level flag to false
        red_in_level[level] = False
    #Of the character is "}"
    elif data[index] == "}":
        #If the number is found save it to the current level
        if len(number) > 0:
            number_per_level[level].append(int(number))
            number = ""
        #If the level flag is true, erase numbers from the current level
        if red_in_level[level]:
            number_per_level[level] = []
            red_in_level[level] = False
        #If the flag is false, copy the numbers to level before
        else:
            number_per_level[level-1] = number_per_level[level-1] + number_per_level[level]
        #Reduce level
        level -= 1
    #If the character is "r" and it is not one of the 2 last characters and we are in object(last parentheses is not "[")
    elif data[index] == "r" and index < (len(data)-2) and parentheses[-1] != "[":
        #If the number is found save it to the current level
        if len(number) > 0:
            number_per_level[level].append(int(number))
            number = ""
        #If word "red" is found
        if data[index:index+3] == "red":
            #Change the flag for the current level to true
            red_in_level[level] = True

    #If the character is "-" and it is followed with a number collect it
    elif data[index] == "-" and index != len(data)-1:
        if data[index+1].isnumeric():
            number += "-"
    #If the character is a number colleclt it
    elif data[index].isnumeric():
        number += data[index]
    #If the number is found save it to the current level
    elif len(number) > 0:
        number_per_level[level].append(int(number))
        number = ""

#Check at the end whether the number is found and save it to the current level if it is
if len(number) > 0:
    number_per_level[level].append(int(number))
    number = ""


number_sum = 0
#Calculate the sum of all numbers in the level zero
for number in number_per_level[0]:
    number_sum += number

print("The sum of all numbers in the document, while ignoreing objects that have 'red' in it, is",number_sum)

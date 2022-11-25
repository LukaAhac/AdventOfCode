# Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. 
# That's where you come in.

# They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. 
# Your first job is to simply find all of the numbers throughout the document and add them together.

# For example:

# [1,2,3] and {"a":2,"b":4} both have a sum of 6.
# [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
# {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
# [] and {} both have a sum of 0.
# You will not encounter any strings containing numbers.

# What is the sum of all numbers in the document?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day12-JSAbacusFramework.io\input.txt") as f:
    data = f.readlines()

#Input is one line
data = data[0]
#List to store numbers
numbers = []
#Number as a string
number = ""

#For each character in data
for index in range(len(data)):

    #If the character is "-" and it is followed with a number collect it
    if data[index] == "-" and index != len(data)-1:
        if data[index+1].isnumeric():
            number += "-"
    #If the character is a number colleclt it
    elif data[index].isnumeric():
        number += data[index]
    #If the character is not a number and there is a number collected, save the number into the list and empty the number string
    elif len(number) > 0:
        numbers.append(int(number))
        number = ""

#Check at the end if there is something in the number string and save it to the list if it is
if len(number) > 0:
    numbers.append(int(number))
    number = ""


number_sum = 0
#Calculate the sum of all numbers in the list
for number in numbers:
    number_sum += number

print("The sum of all numbers in the document is",number_sum)
    
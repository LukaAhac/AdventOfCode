# Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and 
# using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

# Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, 
# and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

# For example:

# 1 becomes 11 (1 copy of digit 1).
# 11 becomes 21 (2 copies of digit 1).
# 21 becomes 1211 (one 2 followed by one 1).
# 1211 becomes 111221 (one 1, one 2, and two 1s).
# 111221 becomes 312211 (three 1s, two 2s, and one 1).
# Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

# Your puzzle input is 1321131112.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

data = "1321131112"

iterations = 40

current_input = data

#For each iteration
for _ in range(iterations):

    #Count the first number
    counter = 1
    #Clear variable for next input
    next_input = ""

    #For each number in the input starting from second
    for index in range(1,len(current_input)):

        #Check if the current number is equal to number before it
        if current_input[index-1] == current_input[index]:
            #If it is count it
            counter += 1
        else:
            #If it is not then append the next input with the counter and previous number, count current number
            next_input += str(counter)+current_input[index-1]
            counter = 1

    #At the end append last counter and number
    next_input += str(counter)+current_input[-1]

    #Prepare the new input for next iteration
    current_input = next_input

print("Length of the result is",len(current_input))



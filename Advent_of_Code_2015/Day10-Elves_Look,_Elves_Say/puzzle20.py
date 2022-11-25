# Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of Life fame).

# Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

data = "1321131112"

iterations = 50

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



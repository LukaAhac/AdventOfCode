# The second disk you have to fill has length 35651584. Again using the initial state in 
# your puzzle input, what is the correct checksum for this disk?

#-----------------------------------------------------------------------------------------------------------

#Given input
data = "10111011111001111"
diskSize = 35651584

#While we do not have enough data, preform the dragon cruve
while len(data) < diskSize:

    #Algorithm specified in instructions
    a = data
    b = data[::-1]
    newB = ""

    for index in range(len(b)):

        if b[index] == "0":
            newB += "1"
        else:
            newB += "0"

    data = a + "0" + newB

#Take exact amount of data that fits on the disk
data = data[:diskSize]

#Until we compute corret checksum
while True:

    #Our checksum string
    checkSum = ""

    #Number of paris in the string
    numberOfPairs = int(len(data)/2)

    #For each pair
    for index in range(numberOfPairs):

        #If the bits in the pair are equal, replace them with 1
        if data[index*2] == data[index*2+1]:
            checkSum += "1"
        #If different replace with 0
        else:
            checkSum += "0"
    
    #If lenght of checksum is odd that is the solution
    if len(checkSum) % 2 == 1:
        break
    #Otherwise if it is even, calculate checksum again
    else:
        data = checkSum

print("The correct checksum is:",checkSum)
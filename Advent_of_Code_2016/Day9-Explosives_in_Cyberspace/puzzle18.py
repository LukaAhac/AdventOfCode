# Apparently, the file actually uses version two of the format.

# In version two, the only difference is that markers within decompressed data are decompressed. 
# This, the documentation explains, provides much more substantial compression capabilities, 
# allowing many-gigabyte files to be stored in only a few kilobytes.

# For example:

# (3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains no markers.
# X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed data from the (8x2) marker is
#  then further decompressed, thus triggering the (3x3) marker twice for a total of six ABC sequences.
# (27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A repeated 241920 times.
# (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445 characters long.
# Unfortunately, the computer you brought probably doesn't have enough memory to actually decompress the file; 
# you'll have to come up with another way to get its decompressed length.

# What is the decompressed length of the file using this improved format?

#-----------------------------------------------------------------------------------------------------------

#Function to recursively decode string
def decodeString(givenString):

    #String length that we are computing
    stringLenght = 0
    #Size of the given compressed string
    size = len(givenString)
   #Variables for the numbers inside the marker brackets (lenghtOfSequence,numberOfRepetitoin)
    lengthOfSequence = 0
    numberOfRepetiton = 0
    #Index in the compressed file
    index = 0

    #While whole string is not read
    while index < size:

        ##If we found a marker
        if givenString[index] == "(":
            index += 1
            aXb = ""

            #Extract the number from the marker
            while givenString[index] != ")":

                aXb += givenString[index]
                index+=1

            lengthOfSequence,numberOfRepetiton = map(int,aXb.split("x"))

            #Call function recursively to compute the length of the subsequent marker
            stringLenght += decodeString(givenString[index+1:index+1+lengthOfSequence])*numberOfRepetiton

            index += 1+lengthOfSequence

        #If there is no marker count the character if it is not the whitespace
        elif not givenString[index].isspace():
            index+=1
            stringLenght += 1
        #If it is whitespace just skip it
        else:
            index += 1

    #Return the lenght of the string
    return stringLenght


#Read input
with open(r"Day9-Explosives_in_Cyberspace\input.txt") as f:
    data = f.readlines()

#Comppressed text
compressedText = data[0]

#Compute the lenght
lengthOfAFile = decodeString(compressedText)

print("The decompressed length of the file using this improved format is:",lengthOfAFile)
# Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in 
# situations like this is to switch to a simple repetition code to get the message through.

# In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), 
# but the data seems quite corrupted - almost too badly to recover. Almost.

# All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:

# eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar
# The most common character in the first column is e; in the second, a; in the third, s, and so on. 
# Combining these characters returns the error-corrected message, easter.

# Given the recording in your puzzle input, what is the error-corrected version of the message being sent?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day6-Signals_and_Noise\input.txt") as f:
    data = f.readlines()

#List of recieved messages
recieved = []
#Preprocess the data
for line in data:

    recieved.append(line.strip())

#Corrected message
error_corrected_message = ""

#For each position of the message
for index in range(len(recieved[0])):

    #Dictionary of found letters at that position
    letters = dict()

    #For each of the recieved messages check what letter is at current position
    for message in recieved:

        if message[index] not in letters:
            letters[message[index]] = 1
        else:
            letters[message[index]] += 1

    #Retrive the found letters
    found_letters = list(letters.keys())

    #Sort it by the time of occurances in descedning order
    found_letters = sorted(found_letters, key = lambda x: letters[x], reverse = True)

    #Add thath letter to the corrected message
    error_corrected_message += found_letters[0]

print("The error-corrected version of the message being sent is:",error_corrected_message)
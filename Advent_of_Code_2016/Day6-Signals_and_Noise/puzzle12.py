# Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.

# In this modified code, the sender instead transmits what looks like random data, but for each character, 
# the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise, 
# you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.

# In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this process 
# for the remaining characters produces the original message, advent.

# Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?

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

    #Sort it by the time of occurances in ascending order
    found_letters = sorted(found_letters, key = lambda x: letters[x])

    #Add thath letter to the corrected message
    error_corrected_message += found_letters[0]

print("The error-corrected version of the message being sent is:",error_corrected_message)
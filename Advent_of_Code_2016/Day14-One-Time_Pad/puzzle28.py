# Of course, in order to make this process even more secure, you've also implemented key stretching.

# Key stretching forces attackers to spend more time generating hashes. Unfortunately, it forces 
# everyone else to spend more time, too.

# To implement key stretching, whenever you generate a hash, before you use it, you first find the
# MD5 hash of that hash, then the MD5 hash of that hash, and so on, a total of 2016 additional hashings. 
# Always use lowercase hexadecimal representations of hashes.

# For example, to find the stretched hash for index 0 and salt abc:

# Find the MD5 hash of abc0: 577571be4de9dcce85a041ba0410f29f.
# Then, find the MD5 hash of that hash: eec80a0c92dc8a0777c619d9bb51e910.
# Then, find the MD5 hash of that hash: 16062ce768787384c81fe17a7a60c7e3.
# ...repeat many times...
# Then, find the MD5 hash of that hash: a107ff634856bb300138cac6568c0f24.
# So, the stretched hash for index 0 in this situation is a107ff.... In the end, you find the original 
# hash (one use of MD5), then find the hash-of-the-previous-hash 2016 times, for a total of 2017 uses of MD5.

# The rest of the process remains the same, but now the keys are entirely different. Again for salt abc:

# The first triple (222, at index 5) has no matching 22222 in the next thousand hashes.
# The second triple (eee, at index 10) hash a matching eeeee at index 89, and so it is the first key.
# Eventually, index 22551 produces the 64th key (triple fff with matching fffff at index 22859.
# Given the actual salt in your puzzle input and using 2016 extra MD5 calls of key stretching, what index 
# now produces your 64th one-time pad key?

#-----------------------------------------------------------------------------------------------------------

import hashlib

#Function that checks if the given string has 3 of the same characters in a row
#Returns the character if it does, None otherwise
def checkFor3Char(strToCheck):

    for index in range(len(strToCheck)-2):
        if strToCheck[index] == strToCheck[index+1] == strToCheck[index+2]:
            return strToCheck[index]

    return None

#Function that checks if the given string has 5 of the given charecters in a row
#Returns True if it does, False otherwise
def checkFor5SpecificChar(strToCheck,specifiedChar):

    for index in range(len(strToCheck)-4):
        if specifiedChar == strToCheck[index] == strToCheck[index+1] == \
        strToCheck[index+2] == strToCheck[index+3] == strToCheck[index+4]:
            return True
    return False

#Input data
salt = "ngcjuoqr"
index = 0
keysRequired = 64
keyIsValidForIndexes = 1000
strechingTime = 2016

#Dictionary to store key candidates with ther repeating chars and indexes
keyCandidates = dict()
#Set to store found keys
keys = set()

#Until we finish the process
while True:

    #The process is over if we examined all of the candidates, and found >= 64 keys
    if len(keyCandidates) == 0 and len(keys) >= keysRequired:
        break
    
    #Construct the string with salt and current index
    currentString = salt + str(index)

    #Comptue the MD5 hash of the current string and represent it in hexadecimal base
    md5hash = hashlib.md5(currentString.encode())
    md5hash = md5hash.hexdigest()

    #Key stretching - Compute the MD5 hash 2016 additional times
    for stretchingIndex in range(strechingTime):
        md5hash = hashlib.md5(md5hash.encode())
        md5hash = md5hash.hexdigest()

    #If we have some key candidates
    if len(keyCandidates) > 0:

        #Check for each
        for candidate in keyCandidates.copy():
            #If its a still valid key candidate due to current index
            if keyCandidates[candidate][1] < index-keyIsValidForIndexes:
                #If not valid delete the candidate
                del keyCandidates[candidate]
            #If it is valid check if the current hash makes it a real key
            elif checkFor5SpecificChar(md5hash,keyCandidates[candidate][0]):
                #Add it and its index to the keys set if it does
                keys.add((candidate,keyCandidates[candidate][1]))
                #And delete from candidates
                del keyCandidates[candidate]

    #Check wheter the current hash has 3 of the same characters in a row
    checker = checkFor3Char(md5hash)

    #If it does and we dont already have specified amount of keys
    if checker is not None and len(keys)<keysRequired:
        #Add it to the candidate dictionary
        keyCandidates[md5hash] = [checker,index]

    #Go to the next index
    index += 1

#Get te list of keys and sort it by the their creation index
keyList = sorted(list(keys),key = lambda x: x[1])

print(keyList[keysRequired-1][1],"is the index that produces 64th one-time pad key!")
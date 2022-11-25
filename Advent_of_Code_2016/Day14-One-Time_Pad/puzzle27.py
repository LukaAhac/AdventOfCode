# In order to communicate securely with Santa while you're on this mission, you've been using a 
# one-time pad that you generate using a pre-agreed algorithm. Unfortunately, you've run out of keys 
# in your one-time pad, and so you need to generate some more.

# To generate keys, you first get a stream of random data by taking the MD5 of a pre-arranged salt 
# (your puzzle input) and an increasing integer index (starting with 0, and represented in decimal); 
# the resulting MD5 hash should be represented as a string of lowercase hexadecimal digits.

# However, not all of these MD5 hashes are keys, and you need 64 new keys for your one-time pad. 
# A hash is a key only if:

# It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
# One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.
# Considering future hashes for five-of-a-kind sequences does not cause those hashes to be skipped; instead, 
# regardless of whether the current hash is a key, always resume testing for keys starting with the 
# very next hash.

# For example, if the pre-arranged salt is abc:

# The first index which produces a triple is 18, because the MD5 hash of abc18 contains ...cc38887a5.... 
# However, index 18 does not count as a key for your one-time pad, because none of the next thousand hashes 
# (index 19 through index 1018) contain 88888.
# The next index which produces a triple is 39; the hash of abc39 contains eee. It is also the first key: 
# one of the next thousand hashes (the one at index 816) contains eeeee.
# None of the next six triples are keys, but the one after that, at index 92, is: it contains 999 and index 

# So, using our example salt of abc, index 22728 produces the 64th key.

# Given the actual salt in your puzzle input, what index produces your 64th one-time pad key?

# Your puzzle input is ngcjuoqr.

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
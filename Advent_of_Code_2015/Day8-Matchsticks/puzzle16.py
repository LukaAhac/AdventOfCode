# Now, let's go the other way. In addition to finding the number of characters of code, you should now encode each code representation as a new 
# string and find the number of characters of the new encoded representation, including the surrounding double quotes.

# For example:

# "" encodes to "\"\"", an increase from 2 characters to 6.
# "abc" encodes to "\"abc\"", an increase from 5 characters to 9.
# "aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
# "\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11.
# Your task is to find the total number of characters to represent the newly encoded strings minus the number of characters of code in 
# each original string literal. For example, for the strings above, the total encoded length (6 + 9 + 16 + 11 = 42) minus the characters in 
# the original code representation (23, just like in the first part of this puzzle) is 42 - 23 = 19.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day8-Matchsticks\input.txt") as f:
    data = f.readlines()

characters_of_code = 0
encoded_string_characters = 0

#For each string in data
for string in data:

    #Remove whitspaces from the ends
    string = string.strip()
    
    #Length of the string is how much he contributes to the charachters of code
    characters_of_code += len(string)

    index = 0
    encoded_string = ""

    #Append starting apostrophe to the encoded string
    encoded_string += '"'

    #For each letter in string
    while index < (len(string)):
        
        #If the letter is apostrophe encode id with \"
        if string[index] == '"':
            encoded_string += r'\"'
        #If the letter is backslash encode it iwth \\
        elif string[index] == "\\":
            encoded_string += r'\\'
        #Else copy the letter
        else:
            encoded_string += string[index]

        index += 1
    
    #Append finishing apostrophe to the encoded string
    encoded_string += '"'
    
    #Add the length of encoded string
    encoded_string_characters += len(encoded_string)

print("The total number of characters to represent the newly encoded strings minus the number of characters of code is",encoded_string_characters-characters_of_code)

# Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.

# It is common in many programming languages to provide a way to escape special characters in strings. For example, C, JavaScript, Perl, Python, 
# and even PHP handle special characters in very similar ways.

# However, it is important to realize the difference between the number of characters in the code representation of the string literal 
# and the number of characters in the in-memory string itself.

# For example:

# "" is 2 characters of code (the two double quotes), but the string contains zero characters.
# "abc" is 5 characters of code, but 3 characters in the string data.
# "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
# "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.
# Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are \\ (which represents a single backslash), 
# \" (which represents a lone double-quote character), and \x plus two hexadecimal characters (which represents a single character with that ASCII code).

# Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for 
# the values of the strings in total for the entire file?

# For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters 
# in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day8-Matchsticks\input.txt") as f:
    data = f.readlines()

characters_of_code = 0
string_characters = 0

#For each string in data
for string in data:

    #Remove whitspaces from the ends
    string = string.strip()
    
    #Length of the string is how much he contributes to the charachters of code
    characters_of_code += len(string)

    index = 0

    #For each letter in string
    while index < (len(string)):

        #If it is an starting or ending apostrophe ignore it and increase index by 1
        if string[index] == '"':
            index += 1
        #If it is one of the escapeing characters then count it as a one character and increase index by 2
        elif string[index:index+2] == r'\\' or string[index:index+2] == r'\"':
            index += 2
            string_characters += 1
        #If it is escapeing character followed by hexadecimal notation count it as an one character and increase index by 4
        elif string[index:index+2] == r'\x':
            index += 4
            string_characters += 1
        #If it is a regular character count it and increase index by one
        else:
            index += 1
            string_characters += 1

print("The number of characters of code for string literals minus the number of characters in memory is",characters_of_code-string_characters)
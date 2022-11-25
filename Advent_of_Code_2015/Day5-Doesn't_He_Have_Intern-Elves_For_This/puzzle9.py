# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:

# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
# How many strings are nice?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day5-Doesn't_He_Have_Intern-Elves_For_This\input.txt") as f:
    data = f.readlines()

nice_strings = 0

#For each string check rules
for string in data:

    vowels = 0
    doubleletter = False
    doesntCotain = True
    
    #For each letter in string
    for index in range(len(string)):
        #RULE1
        #Check if it is a vowel
        if string[index].lower() in ["a","e","i","o","u"]:
            vowels += 1
        #Check if it is not a last letter
        if index != (len(string)-1):
            #RULE2
            #Check if a letter appears twice in a row
            if string[index] == string[index+1]:
                doubleletter = True
            #RULE3
            #Check if it contains a forbiden substring
            if string[index] == "a" and string[index+1] == "b":
                doesntCotain = False
            elif string[index] == "c" and string[index+1] == "d":
                doesntCotain = False
            elif string[index] == "p" and string[index+1] == "q":
                doesntCotain = False
            elif string[index] == "x" and string[index+1] == "y":
                doesntCotain = False
    
    #If any of the three rules are broken it's a naughty string
    if vowels < 3 or not doubleletter or not doesntCotain:
        continue
    #Else it's a nice string
    nice_strings += 1

print(nice_strings,"strings are nice strings.")


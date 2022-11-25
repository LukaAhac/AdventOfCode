# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
# For example:

# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
# xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
# How many strings are nice under these new rules?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day5-Doesn't_He_Have_Intern-Elves_For_This\input.txt") as f:
    data = f.readlines()

nice_strings = 0

#For each string check rules
for string in data:

    doubleletter = False
    repeatingletter = False
    
    #For each letter in string
    for index in range(len(string)):
        #RULE1
        #If it is not one of last three letters
        if index < (len(string)-3):
            #Take a substring of lenght two
            substring = string[index:index+2]
            #For the rest of the string
            for index2 in range(index+2,len(string)):
                #If it is not last letter
                if index2 < (len(string)-1):
                    #Check if taken substring repeats
                    if substring == string[index2:index2+2]:
                        #Change the flag if it does
                        doubleletter = True

        #RULE2
        #If it is not one of last two letters
        if index < (len(string)-2):
            #Check if current letter equals to the letter two places after
            if string[index] == string[index+2]:
                #Change the flag if it doaes
                repeatingletter = True

    
    #If any of the rules are broken it's a naughty string
    if not doubleletter or not repeatingletter:
        continue
    #Else it's a nice string
    nice_strings += 1

print(nice_strings,"strings are nice strings.")


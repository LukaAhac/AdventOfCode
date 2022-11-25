# You would also like to know which IPs support SSL (super-secret listening).

# An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences 
# (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. 
# An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. 
# A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

# For example:

# aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
# xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
# aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because 
# the interior character must be different).
# zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
# How many IPs in your puzzle input support SSL?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
import re

#Read input
with open(r"Day7-Internet_Protocol_Version_7\input.txt") as f:
    data = f.readlines()

#Count for the wanted IPs
IPs_count = 0

#Fore each IP
for line in data:
    #Preprocess the string
    line = line.strip()

    #Find all the string outside of the brackets []
    outside_brackets = re.split("\[[a-z]*\]",line)
    #Find all the string inside the brackets []
    inside_brackets = re.findall("\[[a-z]*\]",line)

    #Set to store found inside BAB substrings
    inside_BAB = set()
    #Set to store found outside ABA strings, but they will be converted to corrseponding BAB string
    outside_ABA_transformed_to_BAB = set()
    
    #For each inside bracket string
    for inside in inside_brackets:

        #Check wheter contains BAB substring or not
        for index in range(len(inside)-2):

            #If it does, save it to the set
            if inside[index] == inside[index+2] and inside[index] != inside[index+1]:

                inside_BAB.add(inside[index]+inside[index+1]+inside[index])

    #Check each outsides string for the ABA substring
    for outside in outside_brackets:

        for index in range(len(outside)-2):

            #If it does have it, save the BAB form of it to the set
            if outside[index] == outside[index+2] and outside[index] != outside[index+1]:

                outside_ABA_transformed_to_BAB.add(outside[index+1]+outside[index]+outside[index+1])

    #If intersection between sets is larger then 0, then the IP supports SSL!
    if len(inside_BAB.intersection(outside_ABA_transformed_to_BAB)) > 0:
        IPs_count += 1

print(IPs_count,"IPs support SSL!")
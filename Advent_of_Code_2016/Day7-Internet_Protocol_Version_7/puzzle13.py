# While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). 
# You'd like to figure out which IPs support TLS (transport-layer snooping).

# An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a 
# pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an 
# ABBA within any hypernet sequences, which are contained by square brackets.

# For example:

# abba[mnop]qrst supports TLS (abba outside square brackets).
# abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
# aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
# ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
# How many IPs in your puzzle input support TLS?

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

    #Flags for the found ABBA substrings
    foundInside = False
    foundOutside = False
    
    #For each inside bracket string
    for inside in inside_brackets:

        #Check wheter contains ABBA substring or not
        for index in range(len(inside)-3):

            if inside[index] == inside[index+3] and inside[index+1] == inside[index+2] and inside[index] != inside[index+1]:

                foundInside = True
                break
        
        if foundInside:
            break
    #If the string is found, continue to the next IP
    if foundInside:
        continue

    #If inside strings do not have ABBA substring, check outsides string for the ABBA substring
    for outside in outside_brackets:

        for index in range(len(outside)-3):

            if outside[index] == outside[index+3] and outside[index+1] == outside[index+2] and outside[index] != outside[index+1]:

                #If it does, increase do count
                foundOutside = True
                IPs_count += 1
                break

        if foundOutside:
            break

print(IPs_count,"IPs support TLS!")
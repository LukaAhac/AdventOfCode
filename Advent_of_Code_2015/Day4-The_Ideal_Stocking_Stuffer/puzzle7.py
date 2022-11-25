# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. 
# The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. 
# To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

# For example:

# If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
# If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, 
# the MD5 hash of pqrstuv1048970 looks like 000006136ef....
# Your puzzle input is iwrupvqb.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

import hashlib

data = "iwrupvqb"

number = 0

#Repeat until you find solution
while True:

    #Find MD5 hash of string+number in hexadecimal shape
    result = (hashlib.md5((data + str(number)).encode())).hexdigest()

    #If it starts with 5 zeros that is the solution
    if result [0:5] == "00000":
        break
    #If not then increase the number
    else:
        number += 1

print("The number that produces required hash is",number)
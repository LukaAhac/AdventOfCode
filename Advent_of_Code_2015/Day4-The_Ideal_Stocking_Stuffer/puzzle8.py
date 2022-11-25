# Now find one that starts with six zeroes.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

import hashlib

data = "iwrupvqb"

number = 0

#Repeat until you find solution
while True:

    #Find MD5 hash of string+number in hexadecimal shape
    result = (hashlib.md5((data + str(number)).encode())).hexdigest()

    #If it starts with 5 zeros that is the solution
    if result [0:6] == "000000":
        break
    #If not then increase the number
    else:
        number += 1

print("The number that produces required hash is",number)
# As the door slides open, you are presented with a second door that uses a slightly more inspired security mechanism. 
# Clearly unimpressed by the last version (in what movie is the password decrypted in order?!), the Easter Bunny engineers 
# have worked out a better solution.

# Instead of simply filling in the password from left to right, the hash now also indicates the position within the password to fill. 
# You still look for hashes that begin with five zeroes; however, now, the sixth character represents the position (0-7), 
# and the seventh character is the character to put in that position.

# A hash result of 000001f means that f is the second character in the password. Use only the first result for each position, 
# and ignore invalid positions.

# For example, if the Door ID is abc:

# The first interesting hash is from abc3231929, which produces 0000015...; so, 5 goes in position 1: _5______.
# In the previous method, 5017308 produced an interesting hash; however, it is ignored, because it specifies an invalid position (8).
# The second interesting hash is at index 5357525, which produces 000004e...; so, e goes in position 4: _5__e___.
# You almost choke on your popcorn as the final character falls into place, producing the password 05ace8e3.

# Given the actual Door ID and this new method, what is the password? Be extra proud of your solution if it uses a cinematic "decrypting" animation.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
import hashlib

#Read input
data = "ojvtpuvg"
#List of code chars
code = [None]*8
#Number of found characters
found_code_numbers = 0
#Current index
index = 0

#Until we found all code characters loop through next
while found_code_numbers != 8:

    #Construct current string
    string = data + str(index)

    #Calcilate MD5 hash and give its hexadecimal representation
    md5_hash = hashlib.md5(string.encode()).hexdigest()

    #If the hash starts with the 5 zeroes
    if md5_hash[:5] == "00000":

        #Try to convert 5th char to integer
        try:
            position = int(md5_hash[5])
            
            #If it is integer but bigger than 8 or the position is already filled just pass
            if position >= 8 or code[position] is not None:
                pass
            #Else fill the position with 6th character
            else:
                code[position] = md5_hash[6]
                found_code_numbers += 1
        #If not possible, pass
        except:
            pass

    #Increase index by 1
    index += 1

print("The password is:","".join(code))
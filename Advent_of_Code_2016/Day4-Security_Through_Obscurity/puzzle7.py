# Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, 
# but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

# Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

# A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. 
# For example:

# aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are 
# listed alphabetically.
# a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
# not-a-real-room-404[oarel] is a real room.
# totally-real-room-200[decoy] is not.
# Of the real rooms from the list above, the sum of their sector IDs is 1514.

# What is the sum of the sector IDs of the real rooms?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
import string

#Read input
with open(r"Day4-Security_Through_Obscurity\input.txt") as f:
    data = f.readlines()

#String of English alphabet
alphabet = string.ascii_lowercase
#Lenght of English alphabet
alphabet_len = len(alphabet)
#Sum od IDs
sum_of_sector_IDs = 0

#For each encryption
for line in data:

    #Dictionary of found letters
    letters = dict()
    #Prepare the string, devide it by dashes
    line = line.strip().split("-")

    #For each substring besides last, becasue last is ID+checksum
    for word in line[:-1]:

        #Split it into letters
        chars = list(word)
        
        #Count the each letter
        for letter in chars:

            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

    #Retrive the list of found letters from the dictionary
    all_letters = list(letters.keys())
    #Sort the letters in desired manner, descending by the time of letter occurance and in case of a tie ascending by the position in the alphabet
    #There is a trick used here, key for sorting is number of letter occurances joined by the letter at oposing place in the alphabet
    #So there is one descending sorting
    all_letters = sorted(all_letters, key=lambda x: str(letters[x])+(alphabet[alphabet_len-alphabet.index(x)-1]),reverse = True)
    #Take the 5 most common letters
    five_most_common = all_letters[:5]
    #Join the letters together
    five_most_common = "".join(five_most_common)

    #Check if they are equal to checksum and add the ID to the sum if they are
    if five_most_common == line[-1][-6:-1]:
        sum_of_sector_IDs += int(line[-1].split("[")[0])

print("The sum of the sector IDs of the real rooms is:",sum_of_sector_IDs)
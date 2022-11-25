# With all the decoy data out of the way, it's time to decrypt this list and get moving.

# The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. 
# However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

# To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. 
# A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

# For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

# What is the sector ID of the room where North Pole objects are stored?

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
#Real rooms
rooms = []

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
        rooms.append(line)

#Decrypted rooms:
decrypted_rooms = dict()

#Decrypth the name of each room
for room in rooms:

    #Empy string for the room name
    room_name = ""
    #Room sector ID
    room_sector_ID = int(room[-1].split("[")[0])

    #For each word in the name
    for word in room[:-1]:
        
        #Move each letter for the value of room sector ID
        for letter in list(word):

            room_name = room_name + alphabet[(alphabet.index(letter)+room_sector_ID)%alphabet_len]

        #Add sapce
        room_name = room_name + " "

    #Remove the last space
    room_name = room_name[:-1]
    #Store the room
    decrypted_rooms[room_name] = room_sector_ID

print("The sector ID of the room where North Pole objects are stored is",decrypted_rooms["northpole object storage"])

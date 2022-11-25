# Santa's previous password expired, and he needs help choosing a new one.

# To help him remember his new password after the old one expires, Santa has devised a method of coming up with a 
# password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), 
# so he finds his new password by incrementing his old password string repeatedly until it is valid.

# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, 
# it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

# Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
# Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
# Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
# For example:

# hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
# abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
# abbcegjk fails the third requirement, because it only has one double letter (bb).
# The next password after abcdefgh is abcdffaa.
# The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
# Given Santa's current password (your puzzle input), what should his next password be?

# Your puzzle input is hepxcrrq.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

data = "hepxcrrq"

#Set starting flah
valid = False
#Set password for first iteration
current_password = data

#While password is not valid
while not valid:

    #Check if the password includes one increasing straight of at least three letters
    for index in range(len(current_password)-2):
        if ord(current_password[index]) == ord(current_password[index+1])-1 and ord(current_password[index]) == ord(current_password[index+2])-2:
            #If it does, set flag to be true
            valid = True
            break
    
    #Make a list of letters
    letters = list(current_password)
    #Check if the password contains i,o or l
    if "i" in letters or "o" in letters or "l" in letters:
        #Set flag to be false
        valid = False

    double_letters = set()
    #Find all different pairs of letters
    for index in range(len(current_password)-1):
        if current_password[index] == current_password[index+1]:
            double_letters = double_letters | {current_password[index]+current_password[index+1]}
    #Check if the password contains at least two different, non-overlapping pairs of letters 
    if len(double_letters) < 2:
        #If not set flag to be false
        valid = False

    #If the current password is not valid, increase it
    if not valid :

        #Starting from the last letter iterate to the first
        for index in range(len(letters)-1,-1,-1):

            #If the letter is "z", change it to "a" and go the the letter before
            if letters[index] == "z":
                letters[index] = "a"
                continue
            #If it is not z, just increment the letter
            else:
                letters[index] = chr(ord(letters[index])+1)
                break
    #Join the list of letters into the string
    current_password = "".join(letters)

print("His next password should be",current_password)

# Santa's password expired again. What's the next one?

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#New input is the old output
data = "hepxxyzz"

#List of expired passwords
expired_passwords = ["hepxxyzz"]

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

    #Check if the password is already expired
    if current_password in expired_passwords:
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
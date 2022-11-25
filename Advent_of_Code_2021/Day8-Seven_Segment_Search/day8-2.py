# Through a little deduction, you should now be able to determine the remaining digits. Consider again the first 
# example above:

# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf
# After some careful analysis, the mapping between signal wires and segments only make sense in the following 
# configuration:

#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc
# So, the unique signal patterns would correspond to the following digits:

# acedgfb: 8
# cdfbe: 5
# gcdfa: 2
# fbcad: 3
# dab: 7
# cefabd: 9
# cdfgeb: 6
# eafb: 4
# cagedb: 0
# ab: 1
# Then, the four digits of the output value can be decoded:

# cdfeb: 5
# fcadb: 3
# cdfeb: 5
# cdbaf: 3
# Therefore, the output value for this entry is 5353.

# Following this same process for each entry in the second, larger example above, the output value of each entry 
# can be determined:

# fdgacbe cefdb cefbgd gcbe: 8394
# fcgedb cgb dgebacf gc: 9781
# cg cg fdcagb cbg: 1197
# efabcd cedba gadfec cb: 9361
# gecf egdcabf bgf bfgea: 4873
# gebdcfa ecba ca fadegcb: 8418
# cefg dcbef fcge gbcadfe: 4548
# ed bcgafe cdgba cbgef: 1625
# gbdfcae bgc cg cgb: 8717
# fgae cfgab fg bagce: 4315
# Adding all of the output values in this larger example produces 61229.

# For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do 
# you get if you add up all of the output values?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day8-Seven_Segment_Search\input.txt") as f:
    data = f.readlines()

#Given input
inp = []

#Parse input
for line in data:
    line = line.strip().split()
    inp.append(line)

#Sum of the output values
suma = 0

#For each line
for line in inp:

    #First 10 digits are input digits
    inpDigits = line[:10]
    #Sorte them by length in descending order
    inpDigits = sorted(inpDigits,key = lambda x: len(x),reverse=True)
    #Last 4 digits are output digits
    outputDigits = line[-4:]

    #Dicionary of digits
    digits = dict()

    #For each digit in input digits, first find 4 unambigous one 
    #unambigous because there is only one digit with that number of elements
    for digit in inpDigits:

        if len(digit) == 2:

            digits["1"] = digit

        elif len(digit) == 3:

            digits["7"] = digit

        elif len(digit) == 4:

            digits["4"] = digit

        elif len(digit) == 7:

            digits["8"] = digit

    #Now deduce the reset
    for digit in inpDigits:

        #We are getting it in desceding order of lenght so we are resolving the digits with the lenght of 6
        #with our four digits that we have from beggining (1,4,7,8)
        if len(digit) == 6:

            #Check if it is 9
            nine = True
            #It is 9 if it contains all of the element that 4 contains as well (Other 6 lenght digits, zero and
            # six does not contain all elements that four contains)
            for letter in digits["4"]:

                if letter not in digit:
                    nine = False

            #If it is 9, save it
            if nine:

                digits["9"] = digit
                continue

            #Now we know that it is not nine, check if it is zero 
            zero = True
            #It is 0 if contains all elements that 1 contains as well, because 6 does not
            for letter in digits["1"]:

                if letter not in digit:
                    zero = False

            #If it is 0, save it
            if zero:

                digits["0"] = digit
                continue

            #Else it is 6
            digits["6"] = digit

        #Now we resolve those with the lenght of five
        elif len(digit) == 5:

            #Check for 3 first
            three = True
            #It is 3 if it contains all the elements that 1 contains as well, because that is not true for 2 and 5
            for letter in digits["1"]:

                if letter not in digit:
                    three = False

            #If it is 3, save it
            if three:

                digits["3"] = digit
                continue

            #Check for five now - we have to distinct 5 and 2 now
            five = True

            #We will distinct 5 and 2 by wheter or not it contains right lower part, it is 5 if it contains it
            #Since we do not know the name of the right lower part, we know that that part is the only part
            #that 1 and 6 share, so 5 must share it aswell in order to be 5, else its 2
            for letter in digits["1"]:

                if letter in digits["6"] and letter not in digit:

                    five = False

            #If it is 5, save it
            if five:
            
                digits["5"] = digit
                continue

            #Else it is 2
            digits["2"] = digit

    
    #String to represent the number
    digitString = ""

    #List of (num,code) elements
    keyVal = []

    #Map->list
    for key in digits:
        keyVal.append((key,"".join(sorted(digits[key]))))

    #Resolve 4 output values
    for digit in line[-4:]:

        #Append output values to the string representation
        for elem in keyVal:

            if elem[1] == "".join(sorted(digit)):
                digitString += elem[0]
    
    #Add the integer to the sum
    suma += int(digitString)
    
print("If I add up all of the output values, I get :",suma)
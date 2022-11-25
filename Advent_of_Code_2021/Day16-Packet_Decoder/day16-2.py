# Now that you have the structure of your transmission decoded, you can calculate the value of the expression it represents.

# Literal values (type ID 4) represent a single number as described above. The remaining type IDs are more interesting:

# Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have 
# a single sub-packet, their value is the value of the sub-packet.
# Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their 
# sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
# Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
# Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
# Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than 
# the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
# Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the 
# value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
# Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the 
# value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
# Using these rules, you can now work out the value of the outermost packet in your BITS transmission.

# For example:

# C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
# 04005AC33890 finds the product of 6 and 9, resulting in the value 54.
# 880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
# CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
# D8005AC2A8F0 produces 1, because 5 is less than 15.
# F600BC2D8F produces 0, because 5 is not greater than 15.
# 9C005AC2F8F0 produces 0, because 5 is not equal to 15.
# 9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.
# What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission?

#----------------------------------------------------------------------------------------------------------------------

#Read input
with open(r"Day16-Packet_Decoder\input.txt") as f:
    data = f.readlines()

#Given input
inp = []

#Parse input
for line in data:
    line = line.strip()
    inp.append(line)

inp = inp[0]

#Transform hex to bin, fist two chars will be 0b so ignore that
binary = bin(int(inp,16))[2:]

#Upper transformation ignores leading zeros so add them manually
while len(binary) < len(inp)*4:
    binary = "0"+binary

#Function to recursively evalute packets
def evaluatePacket(bits,startingIndex):

    index = startingIndex
    
    #Get the version and packetID
    pacektVersion = bits[index:index+3]
    pacektVersion = int(pacektVersion,2)
    index += 3
    packetID = bits[index:index+3]
    packetID = int(packetID,2)
    index += 3

    #If packet is ID == 4 then it is a Litreal packet
    #Return the litreal value,index of the next packet
    if packetID == 4:

        more = True
        litralBits = ""

        #Get the bits of the litreal from the blocks of the length of five
        while more:

            if bits[index] == "0":
                more = False
            
            litralBits += bits[index+1:index+5]
            index += 5

        return (int(litralBits,2),index)

    #Else it is the opreator packet
    else:
        
        #Get the value of the 7th bith
        i = bits[index]
        index += 1
        subPacketValues = []
        subPacketLengt = 0

        #If 7th bith is 0 convert next 15 bits to dec
        #Then read subpackets until we reach that length
        if i == "0":

            lenInBits = bits[index:index+15]
            index += 15
            lenInBits = int(lenInBits,2)

            while subPacketLengt != lenInBits:
                val,nextInd = evaluatePacket(bits,index)
                subPacketValues.append(val)
                subPacketLengt += nextInd-index
                index = nextInd

        #If the 7th bit is 1, covnert next 11 bits to dec
        #Then read that amount of subpackets
        else:

            numOfSubpacks = bits[index:index+11]
            index += 11
            numOfSubpacks = int(numOfSubpacks,2)

            while len(subPacketValues) != numOfSubpacks:
                val,nextInd = evaluatePacket(bits,index)
                subPacketValues.append(val)
                subPacketLengt += nextInd-index
                index = nextInd

        #Performe operations on the subpackets corrsepoding to packet ID
        if packetID == 0:
            val =  sum(subPacketValues)
        elif packetID == 1:
            prod = 1
            for pack in subPacketValues:
                prod *= pack
            val =  prod
        elif packetID == 2:
            val =  min(subPacketValues)
        elif packetID == 3:
            val =  max(subPacketValues)
        elif packetID == 5:
            val =  1 if subPacketValues[0] > subPacketValues[1] else 0
        elif packetID == 6:
            val =  1 if subPacketValues[0] < subPacketValues[1] else 0
        elif packetID == 7:
            val =  1 if subPacketValues[0] == subPacketValues[1] else 0

        #Return the value of the packet and index of the next packet
        return (val,index)


print("If we evaluate the expression represented by our hexadecimal-encoded BITS transmission we get :", \
    evaluatePacket(binary,0)[0])
from Part1 import LiteralValue


class Packet:
    
    def __init__(self, input):
        self.packet = input

    def GetInput(self):
        binary = str(self.packet)

        return binary
    
    def PacketVersion(self):
        packet = str(self.packet)[: 3]

        return int(packet, 2)

    def PacketTypeID(self):
        typeID = str(self.packet)[3: 6]

        return int(typeID, 2)

    def LiteralValue(self):
        value = ""
        index = 6
        indexToAdd = 0
        while index < len(self.packet):
            if self.packet[index] == "1":
                index += 1
                value += str(self.packet[index : index + 4])
                index += 4
                indexToAdd += 5
            else:
                index += 1
                value += str(self.packet[index : index + 4])
                index += 4
                indexToAdd += 6
                break
        return int(value, 2), indexToAdd

    def Operator(self):
        index = 6
        lengthTypeID = str(self.packet[index])
        zero = False
        indexToAdd = 0
        if lengthTypeID == "0":
            index += 1
            lengthOfSubPackets = int(self.packet[index : index + 15], 2)
            indexToAdd += 17
            zero = True
            return lengthOfSubPackets, zero, indexToAdd
        
        else:
            index += 1
            numberOfPackets = int(self.packet[index : index + 11], 2)
            indexToAdd += 13
            return numberOfPackets, zero, indexToAdd


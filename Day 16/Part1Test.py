from ensurepip import version
from struct import pack
import packet

def main():
    input = GetInput()

    binaryValue = HexToBin(input)

    actualPacket = packet.Packet(binaryValue)

    globalIndex = 0

    versions = []
    typeIDs = []
    literalValues = []

    
    maxIndex = len(binaryValue)
    
    Decode(actualPacket, versions)
    # while globalIndex < maxIndex:
    #     versions.append(actualPacket.PacketVersion())
    #     typeIDs.append(actualPacket.PacketTypeID())
    #     #print(binaryValue[globalIndex:])
    #     globalIndex += 5                               #Packet version and type ID take on 6 bits (bit zero counts as 1)
    #     if actualPacket.PacketTypeID() == 4:
    #         value, indexToAdd = actualPacket.LiteralValue()
    #         print(actualPacket.LiteralValue())
    #         literalValues.append(value)
    #         globalIndex += indexToAdd
    #         actualPacket = packet.Packet(binaryValue[globalIndex:])
    #     else:
    #         value, zero, indexToAdd = actualPacket.Operator()
    #         globalIndex += indexToAdd
    #         if zero:
    #             actualPacket = packet.Packet(binaryValue[globalIndex:])
    #         else:
    #             actualPacket = packet.Packet(binaryValue[globalIndex:])
        
    #     if int(binaryValue[globalIndex:], 2) == 0:
    #         break

    answer = sum(versions)
    #print(answer)
    

def Decode(actualPacket : packet , versions, length = 0):
    print(actualPacket.GetInput())
    packetVersion = actualPacket.PacketVersion()
    typeID = actualPacket.PacketTypeID
    length += 5
    binaryValue = actualPacket.GetInput()
    versions.append(packetVersion)
    

    if actualPacket.PacketTypeID() == 4:
        value, indexToAdd = actualPacket.LiteralValue()
        print(actualPacket.LiteralValue())
        #literalValues.append(value)
        length += indexToAdd
        return length
    else:
        value, zero, indexToAdd = actualPacket.Operator()
        length += indexToAdd
        if zero:
            subPacketLength = 0
            while subPacketLength < value:
                actualPacket = packet.Packet(binaryValue[length + subPacketLength: length + value + subPacketLength])
                subPacketLength = Decode(actualPacket, versions, subPacketLength)
                print(subPacketLength)
            length += subPacketLength
        else:
            subPacketLength = 0
            numberOfPackets = 1
            while numberOfPackets <= value:
                print("length {}, subLength {}".format(length, subPacketLength))
                print("binary value next packet: ", binaryValue[length + subPacketLength:])
                actualPacket = packet.Packet(binaryValue[length + subPacketLength:])
                subPacketLength = Decode(actualPacket, versions)
                numberOfPackets += 1
            length += subPacketLength

    # if int(binaryValue[length:], 2) == 0:
    #     return
    print(versions)
    return length



def GetInput():
    rawInput = open("input").read()
    return rawInput


def HexToBin(input):
    size = len(input) * 4
    integer = int(input, 16)
    binary = bin(integer)[2:].zfill(size)             #pad with left zeros lost on conversion
    return binary






if __name__ == "__main__":
    main()
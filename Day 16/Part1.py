
def main():
    input = GetInput()

    binaryValue = HexToBin(input)

    globalIndex = 0
    versions = []
    typeIDs = []

    while globalIndex < len(binaryValue):
        print(globalIndex)
        isSubPacket = False
        globalIndex = UnpackPacket(binaryValue, globalIndex, versions, typeIDs, isSubPacket)

    print(versions, typeIDs)


def UnpackPacket(binaryValue, globalIndex, versions, typeIDs, isSubPacket):
    literalFlagValue, globalIndex = PacketVersionAndTypeID(binaryValue, globalIndex, versions, typeIDs)

    if literalFlagValue:
        globalIndex = LiteralValue(binaryValue, globalIndex)
    else:
        globalIndex = Operator(binaryValue, globalIndex, versions, typeIDs)


    return globalIndex



def GetInput():
    rawInput = open("testInput.txt").read()
    return rawInput


def HexToBin(input):
    size = len(input) * 4
    integer = int(input, 16)
    binary = bin(integer)[2:].zfill(size)             #pad with left zeros lost on conversion
    return binary


def PacketVersionAndTypeID(binary, globalIndex, versionList, typeIDList):
    bitsToRepresent = 3

    literalValueFlag = False

    packetVersionBin = str(binary)[globalIndex : bitsToRepresent]
    typeIDBin = str(binary)[globalIndex + bitsToRepresent : globalIndex + (bitsToRepresent*2)]
    
    packetVersion = int(packetVersionBin, 2)
    typeID = int(typeIDBin, 2)

    versionList.append(packetVersion)
    typeIDList.append(typeID)

    if typeID % 4 == 0:
        literalValueFlag = True
    
    globalIndex += bitsToRepresent*2
    return literalValueFlag, globalIndex

def LiteralValue(binary, globalIndex):
    while globalIndex < len(binary):
        if binary[globalIndex] == "1":
            number = binary[globalIndex + 1 : globalIndex + 5]
            print(number)
            globalIndex += 5
        elif binary[globalIndex] == "0":
            number = binary[globalIndex + 1 : globalIndex + 5]
            print(number)
            globalIndex += 5
            break
    while globalIndex % 4 != 0:
        globalIndex += 1
    return globalIndex

def Operator(binary, globalIndex, versions, typeIDs):
    lengthTypeID = binary[globalIndex]
    if lengthTypeID == '0':
        lengthOfSubs = int(binary[globalIndex : globalIndex + 16], 2)
        globalIndex += 16
        while globalIndex < globalIndex + 28:
            print(globalIndex)
            globalIndex = UnpackPacket(binary, globalIndex, versions, typeIDs)
    else:
        ...
    return globalIndex


if __name__ == "__main__":
    main()
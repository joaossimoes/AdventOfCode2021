

def main():
    input = GetInput()

    binaryValue = HexToBin(input)
    binaryList = [i for i in binaryValue]
    versions = []

    
    Parse(binaryList, versions)
    #print(versions)
    print(sum([int(i, 2) for i in versions]))
 

def Parse(binaryList, versions):
    while len(binaryList) > 0 :
        if Verify(binaryList):
            return


        version, typeID = GetTypeIDAndVersion(binaryList)
        versions.append(version)
        #print(version, typeID)
        
        if int(typeID, 2) == 4:
            literalNumber = GetTypeID4(typeID, binaryList)

        else:
            lengthOrNumber, operatorType = GetTypeIDNot4(binaryList)

            if operatorType == 0:
                Parse(binaryList[:lengthOrNumber], versions)
                for i in range(lengthOrNumber):
                    if Verify(binaryList):
                        return
                    binaryList.pop(0)
            else:
                for counter in range(lengthOrNumber):
                    Parse(binaryList, versions)
    
        # if Verify(binaryList):
        #     break

        

    

def Verify(binaryList):
    finalstr = ''
    for i in range(len(binaryList)):
        finalstr += binaryList[i]
    if int(finalstr, 2) == 0:
        return 1
    return 0



def GetTypeIDAndVersion(binaryList):
    version = ""
    typeID = ""
    for i in range(3):
        version += binaryList.pop(0)
    for i in range(3):
        typeID += binaryList.pop(0)

    return version, typeID


def GetTypeID4(typeID, binaryList):
    literalNumber = ''
    prefix = 1

    while prefix != 0:
        prefix = int(binaryList.pop(0))

        for i in range(4):
            literalNumber += binaryList.pop(0)


    return literalNumber


def GetTypeIDNot4(binaryList):
    lengthTypeID = int(binaryList.pop(0))

    if lengthTypeID == 0:
        subLength = ''
        for i in range(15):
            subLength += binaryList.pop(0)
        return int(subLength, 2), 0

    else:
        subNumber = ''
        for i in range(11):
            subNumber += binaryList.pop(0)
        return int(subNumber, 2), 1
        



def GetInput():
    with open("input") as f:
        rawInput = f.readlines()
    return rawInput[0].strip()


def HexToBin(input):
    size = len(input) * 4                             #AAA # 3*4
    integer = int(input, 16)
    binary = bin(integer)[2:].zfill(size)             #pad with left zeros lost on conversion
    return binary



















if __name__ == "__main__":
    main()
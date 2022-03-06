import re

def main():
    input = open("input")
    coordList = CreateCoordList(input)
    affectedPoints = AffectedPoints(coordList)
    result = GetResult(affectedPoints)
    #print(affectedPoints, len(affectedPoints))
    print(result) 

#Returns a list of all values to analyze (horizontals, verticals and for part 2 only diagonals)
def CreateCoordList(input):
    coordList = []
    for line in input:
        line = line.strip()
        startPos, endPos = re.split('->' , line)
        startPos = startPos.replace(",", ".", 1)
        endPos = endPos.replace(",", ".", 1)
        x1, y1 = str(startPos).split(".")
        x2, y2 = str(endPos).split(".")
        if int(x1) - int(x2) == 0:
            coordList.append([startPos, endPos])
        elif int(y1) - int(y2) == 0:
            coordList.append([startPos, endPos])
        #-------------------------------THIS IF IS WHAT MAKES PART 2------------------------------------------------
        if abs(int(x1) - int(x2)) == abs(int(y1) - int(y2)):     
            coordList.append([startPos, endPos])
    return coordList

#Returns a dictionay with {coordinate:number of lines}
def AffectedPoints(coordList) :
    affectedPoints = {}
    for i in range(len(coordList)):
        startPos = coordList[i][0].strip()
        endPos = coordList[i][1].strip()
        x1, y1 = str(startPos).split(".")
        x2, y2 = str(endPos).split(".")
        
        while int(x1) != int(x2) or int(y1) != int(y2):
            #start the while by adding the coordenates to the dictionary
            if str(startPos) in affectedPoints:
                affectedPoints[str(startPos)] += 1
            else:
                affectedPoints[str(startPos)] = 1
            
            #Checks what are the coordinates the need to update and update them accordingly
            #example: if we have (180,17 -> 167,17) we need to update the X variable until x1 = x2
            if int(y2) < int(y1):
                y1 = int(int(y1) - 1)
                startPos = str(str(x1) + "." + str(y1))
            elif int(y2) > int(y1):
                y1 = int(int(y1) + 1)
                startPos = str(str(x1) + "." + str(y1))
            
            if int(x2) < int(x1):
                x1 = int(int(x1) - 1)
                startPos = str(str(x1) + "." + str(y1))
            elif int(x2) > int(x1):
                x1 = int(int(x1) + 1)
                startPos = str(str(x1) + "." + str(y1))

            #we check again to see if all coordinates ar equal because if they are we won't enter the while again and we haven't added nothing to the dictionary
            if int(x1) == int(x2) and int(y1) == int(y2):
                if str(startPos) in affectedPoints:
                    affectedPoints[str(startPos)] += 1
                else:
                    affectedPoints[str(startPos)] = 1
    return affectedPoints

#Returns result which is a counter of all the values in the dictionary that are bigger than 1
def GetResult(dict):
    result = 0
    for value in dict.values():
        if value > 1:
            result += 1
    return result


if __name__ == "__main__":
    main()
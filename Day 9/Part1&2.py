import math

def main():
    input = open("input")

    inputList = TreatInput(input)
    lowPoints, coordOfLowPoints = FindLowPoints(inputList)
    sumOfRiskLevel = RiskLevel(lowPoints)
    print("part 1 has a result of: ", sumOfRiskLevel)
    basins = FindBasins(inputList, coordOfLowPoints)
    threeLargest = ThreeLargest(basins)
    result = MultThreeLargest(threeLargest)
    print("part 2 has a result of: ", result)

#region "part 1"
def TreatInput(input):
    inputList = []
    for line in input:
        inputList.append(line.strip())
    return inputList

def FindLowPoints(inputList):
    x = 0
    y = 0
    listOfPoitns = []
    coordOfLowPoints = []
    while y < len(inputList):
        if CheckRight(x, y, inputList) and CheckTop(x, y, inputList) and CheckLeft(x, y, inputList) and CheckBottom(x, y, inputList):
            listOfPoitns.append(inputList[y][x])
            coordOfLowPoints.append((x,y))
        x += 1
        if x >= len(inputList[y]):
            y += 1
            x = 0
    return listOfPoitns, coordOfLowPoints


def RiskLevel(listOfPoints):
    sumOfRisk = 0
    for number in listOfPoints:
        risk = int(number) + 1
        sumOfRisk += risk
    return sumOfRisk

def CheckRight(x, y, inputList):
    if int(x + 1) >= len(inputList[y]):
        return True
    if int(inputList[y][x]) < int(inputList[y][x + 1]):
        return True
    else:
        return False

def CheckLeft(x, y, inputList):
    if int(x - 1) < 0:
        return True
    if int(inputList[y][x]) < int(inputList[y][x - 1]):
        return True
    else:
        return False

def CheckBottom(x, y, inputList):
    if int(y + 1) >= len(inputList):
        return True
    if int(inputList[y][x]) < int(inputList[y + 1][x]):
        return True
    else:
        return False

def CheckTop(x, y, inputList):
    if int(y - 1) < 0:
        return True
    if int(inputList[y][x]) < int(inputList[y - 1][x]):
        return True
    else:
        return False
#endregion

#region "part 2"
def FindBasins(inputlist, coordOfLowPoints):
    basins = []
    for lowPoint in coordOfLowPoints:
        basin = []
        newPoints = [lowPoint]
        while True:
            #TODO: CHECK FOR NINES. IF NOT NINE WE ADD THIS TO THE BASIN AND NEW POINTS
            tempNewPoints = []
            for newPoint in newPoints:
                x, y = newPoint
                #IF NINES ARE NOT FOUND AND THE COORD WE ARE VIEWING IS NOT ON THE POINTS OR BASIN WE APPEND THAT POINT TO TEMPNEWPOINTS (THESE ARE THE POINTS WE WILL ANALIZE NEXT CYCLE)
                if (not CheckRightNine(x, y, inputlist)):
                    if (x+1, y) not in basin and (x+1, y) not in tempNewPoints:
                        tempNewPoints.append((x + 1, y))

                if (not CheckBottomNine(x, y, inputlist)):
                    if (x, y+1) not in basin and (x, y+1) not in tempNewPoints:
                        tempNewPoints.append((x, y + 1))

                if (not CheckLeftNine(x, y, inputlist)):
                    if (x-1, y) not in basin and (x-1, y) not in tempNewPoints:
                        tempNewPoints.append((x - 1, y))

                if (not CheckTopNine(x, y, inputlist)):
                    if (x, y-1) not in basin and (x, y-1) not in tempNewPoints:
                        tempNewPoints.append((x, y - 1))
            #IF TEMPNEWPOINTS IS NOT NULL WE KNOW THAT WE WILL HAVE MORE POINTS TO ANALYZE ON THE NEXT CYCLE
                #SO WE APPEND ALL THE POINTS WE FOUND ON A BASIN
            if len(tempNewPoints) > 0:
                newPoints = tempNewPoints.copy()
                for point in newPoints:
                    basin.append(point)
            #IF THERE ARE NO NEW POINTS WE HAVE A FULL BASIN
                #SO WE APPEND THE ACTUAL BASIN TO A LIST OF ALL BASINS AND WE BREAK THE WHILE CYCLE (BUT GO FOR THE NEXT LOW POINT)
            else:
                basinToAdd = basin.copy()
                basins.append(basinToAdd)
                basin.clear()
                break
    return basins        
                

#region "Checks for each side"
def CheckRightNine(x, y, inputList):
    if int(x + 1) >= len(inputList[y]):
        return True
    if int(inputList[y][x+1]) != int(9):
        return False
    else:
        return True

def CheckLeftNine(x, y, inputList):
    if int(x - 1) < 0:
        return True
    if int(inputList[y][x - 1]) != 9:
        return False
    else:
        return True

def CheckBottomNine(x, y, inputList):
    if int(y + 1) >= len(inputList):
        return True
    if int(inputList[y + 1][x]) != 9:
        return False
    else:
        return True

def CheckTopNine(x, y, inputList):
    if int(y - 1) < 0:
        return True
    if int(inputList[y - 1][x]) != 9:
        return False
    else:
        return True
#endregion

def ThreeLargest(basins):
    threeLargest = []
    minValue = math.inf
    for basin in basins:
        if len(threeLargest) < 3:
            threeLargest.append(len(basin))
            if len(basin) < minValue:
                minValue = len(basin)
        elif len(basin) > minValue:
            for i in range(len(threeLargest)):
                if threeLargest[i] == minValue:
                    threeLargest[i] = len(basin)
                    minValue = min(threeLargest)
                    break
    return threeLargest

def MultThreeLargest(threeLargest):
    result = 1
    for number in threeLargest:
        result *= int(number)
    return result

#endregion
if __name__ == "__main__":
    main()
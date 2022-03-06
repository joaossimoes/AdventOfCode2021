import math

def main():
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]

    listInput = TreatInput()
    errorsList, missingList = FindError(listInput, openers, closers)
    GetResult(errorsList)
    GetResultPart2(missingList)


def TreatInput():
    rawInput = open("input")
    listInput = []
    for line in rawInput:
        listInput.append(line.strip())
    return listInput


def FindError (listInput, openers, closers):
    listOfExpected = []
    tempList = []
    expected = ""
    errors = []
    for line in listInput:
        flag = True        
        for bracket in line:
            if bracket in openers:
                for j in range(len(openers)):
                    if str(bracket) == str(openers[j]):
                        listOfExpected.append(closers[j])
                        break

            elif bracket in closers:
                expected = listOfExpected[-1]
                if  expected != bracket:
                    errors.append(bracket)
                    flag = False
                    break
                else:
                    listOfExpected.pop()

        if len(listOfExpected) != 0 and flag:
            tempList.append(listOfExpected.copy())

        listOfExpected.clear()
    return errors, tempList

def GetResult(errors):
    result = 0
    points = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
    for bracket in errors:
        result += points[bracket]
    print(result)

def GetResultPart2(missingList):
    listOfResults = []
    result = 0
    points = {")" : 1, "]" : 2, "}" : 3, ">" : 4}
    for completionString in missingList:
        for bracket in completionString[::-1]:
            result = (result * 5) + points[bracket]
        listOfResults.append(result)
        result = 0
    #SORT THE LIST
    resultsSorted = sorted(listOfResults)
    print(resultsSorted[ math.floor(len(resultsSorted)/2) ])
    

if __name__ == "__main__":
    main()
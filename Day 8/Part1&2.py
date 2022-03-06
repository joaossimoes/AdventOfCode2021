
from typing import final


def main():
    #TODO: FOR NOW IM THINKING THAT THE BEST WAY TO ORGANIZE THE DATA IS WITH A TUPLES LIST (LIST = (PATTERNS, OUTPUT))
    #TODO: I MIGHT NEED TO SEPARATE THIS IN MORE WAYS SO THAT I CAN CHECK VALUE FOR VALUE
    listInput = TreatInput()
    #TODO: AT FIRST GLANCE PART 1 SEEMS TO ONLY NEED THE OUTPUTS AND IT LOOKS LIKE WE ONLY NEED TO CHECK THE LENGHT OF EACH OUTPUT SO I'LL LOOK INTO THAT APPROACH
    resultP1 = Part1(listInput)
    #print(resultP1)
    finalResult = Part2(listInput)
    print(finalResult)


def TreatInput():
    input = open("input")
    inputList = []
    for line in input:
        pattern, output = line.strip().split(" | ")
        inputList.append((pattern, output))
    return inputList


def Part1(listInput):
    result = 0
    for pattern, output in listInput:
        values = output.split(" ")
        for value in values:
            if len(value) == 2 or len(value) == 3 or len(value) == 4 or len(value) == 7:
                result += 1
    return result
    
def Part2(listInput):
    finalResult = 0
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    six = ""
    seven = ""
    eight = ""
    nine = ""
    zero = ""
    for pattern, output in listInput:
        values = pattern.split(" ")
        outputs = output.split(" ")
        for value in values:
            if len(value) == 2:
                one = value
            if len(value) == 4:
                four = value
            if len(value) == 7:
                eight = value
            if len(value) == 3:
                seven = value
        i, j = one[0], one[1]
        topRight, bottomRight = FindBottomAndTopRight(values, i, j)
        two, three = FindThreeAndTwo(values, topRight, bottomRight)
        five, six = FindFiveAndSix(values, topRight, bottomRight)
        zero, nine = FindZeroAndNine(values, topRight, bottomRight, six, three)
        dictOfPatterns = {zero : '0', one : '1', two : '2', three : '3', four : '4', five : '5', six: '6', seven : '7', eight : '8', nine : '9'}
        outputNumber = GetOutputs(outputs, dictOfPatterns)
        finalResult += int(outputNumber)
    return finalResult

    
#We find which patterns correspond to three and two by this logic:
    #three is the only one with a length of five sectors AND with the same sectors of one
    #two is THE ONLY NUMBER that dos not use the sector that's on the bottom right of the display
def FindThreeAndTwo(values, top, bottom):
    for value in values:
        if top in value and bottom in value and len(value) == 5:
            three = value
        if bottom not in value:
            two = value
    return two, three

#To find the five and six we go by the following logic:
    #they are THE ONLY ONES that do not need the top right segment to be represented
    #five has a length of five 
    #six has a length of six
def FindFiveAndSix(values, top, bottom):
    for value in values:
        if top not in value:
            if len(value) == 5:
                five = value
            else:
                six = value
    return five, six

#To find the zero and nine:
    #We isolate both by knowing that they have a length of 6 and are not 6 (we already know the string that represents 6)
    #after that we use the string of three:
        #we know that nine is equal to three but with one more segment
        #based on that we count how many segments are equal to the ones that represent the three and we find nine and zero based on that
def FindZeroAndNine(values, topRight, bottomRight, six, three):
    counter = 0
    for value in values:
        if len(value) == 6 and value is not six:
            i = 0
            while i < len(three):
                if three[i] in value:
                    counter += 1
                i += 1
            if counter == 5:
                nine = value
                counter = 0
            else:
                zero = value
                counter = 0
    return zero, nine

#we find the top right segment and bottom right segment by knowing that bottom right appears more times
def FindBottomAndTopRight(values , i, j):
    counterI = 0
    counterJ = 0
    bottomRight = ""
    topRight = ""
    for value in values:
        if i in value:
            counterI += 1
        if j in value:
            counterJ += 1
    if counterI < counterJ:
        topRight = i
        bottomRight = j
    else:
        topRight = j
        bottomRight = i
    return topRight, bottomRight

#based on the key of patterns that we now know we calculate the numbers on the display
def GetOutputs(outputs, dictOfPatterns):
    result = ''
    for output in outputs:
        for pattern in dictOfPatterns:
            # set() allows to compare strings easily
                if set(output) == set(pattern):
                    result += dictOfPatterns[pattern]
    return result

if __name__ == "__main__":
    main()
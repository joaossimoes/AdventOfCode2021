def main():
    #put the input in list form 
    input = GetInputList()
    recursiveCounter = 0
    oxygenRating = input.copy()
    CO2Rating = input.copy()
    resultOxygen= ""
    resultCO2 = ""

    while recursiveCounter < 12:

        #Check which number is common
        oneIsCommon, allEqualFlag = CheckCommon(oxygenRating, recursiveCounter)

        #we use the Shrink the list function on the oxygen list
        oxygenRating = ShrinkTheList(oneIsCommon, oxygenRating, recursiveCounter)


        oneIsCommon, allEqualFlag = CheckCommon(CO2Rating, recursiveCounter)
        
        #Invert the common variable to find the less common
        if oneIsCommon:
            oneIsCommon = False
        else:
            oneIsCommon = True

        # As we are trying to find the least common variable this flag serves as a safety net for situations where the least common doens't appear at all
        if not allEqualFlag:
            CO2Rating = ShrinkTheList(oneIsCommon, CO2Rating, recursiveCounter)
            
        #Here we check if we have an answer or not, if we do we store it
        oxygenRatingSize = len(oxygenRating)
        CO2RatingSize = len(CO2Rating)
        if oxygenRatingSize == 1 and CO2RatingSize == 1:
            resultOxygen = oxygenRating[0]
            resultCO2 = CO2Rating[0]
        
        recursiveCounter += 1
    #Print the asnwer
    print(int(resultOxygen, 2) * int(resultCO2, 2))


#Get the input into a list
def GetInputList():
    input = open("input")

    lista = []

    for number in input:
        number = number.strip('\n')
        lista.append(number)
    return lista

#Check the most common bit in a place and return two flags. One tells us if the common bit is "1" the other tells us if the bits are all the same
def CheckCommon(listToCheck, recursiveCounter):
    counter = 0
    oneIsCommon = False
    allEqualFlag = False
    #check most common
    for number in listToCheck:
        if number[recursiveCounter] == "1":
            counter += 1
    
    if counter >= len(listToCheck)/2:
        oneIsCommon = True

    #check if bits are all the same
    if counter == len(listToCheck) or counter == 0:
        allEqualFlag = True
    return oneIsCommon, allEqualFlag

#function to shrink the lists based on all the info we have so far
def ShrinkTheList(oneIsCommon, listToShrink, recursiveCounter):
    #if list is already shrunk to size one we skip this step
    if len(listToShrink) == 1:
        return listToShrink
    
    #remove number by number where bit equals "0"
    if oneIsCommon:
        for number in list(listToShrink):
            if number[recursiveCounter] != "1":
                listToShrink.remove(number)
    #remove number by number where bit equals "1"
    else:
        for number in list(listToShrink):
            if number[recursiveCounter] == "1":
                listToShrink.remove(number)
    return listToShrink        
   

if __name__ == "__main__":
    main()
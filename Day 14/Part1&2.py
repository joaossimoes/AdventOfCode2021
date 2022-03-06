import math

def main():
    steps = 40
    template, formulas, numberOfLetters, increasedLetters = TreatInput()
    allPairsQuantity = KnowAmmountOfPairs(template)
    totalEachLetter = BuildPolymer(allPairsQuantity, formulas, steps, numberOfLetters, increasedLetters)
    MostMinusLeast(totalEachLetter)
    

def TreatInput():
    rawInput = open("input")
    counter = 0
    processResults = {}
    increases = {}
    numberOfLetters = {}
    for line in rawInput:
        if counter == 0:
            template = line.strip()
            for letter in template:
                if letter in numberOfLetters:
                    numberOfLetters[letter] += 1
                else:
                    numberOfLetters[letter] = 1
        elif counter > 1:
            pair, intersection = line.strip().split("->")
            pair = pair.strip()
            intersection = intersection.strip()
            increases[pair] = intersection
            newPoli = pair[0] + intersection + pair[1]
            processResults[pair] = [''.join(pair) for pair in zip(newPoli[:-1], newPoli[1:])]
        counter += 1
    return template, processResults, numberOfLetters, increases

#explanation for the line where join is used (when string is NNCB)
    #string[:-1], string[1:] gives ('NNC', 'NCB')
    #then with the zip function it becomes [('N', 'N'), ('N', 'C'), ('C', 'B')]
    #after that we use join to join the tuples and convert those to string

def KnowAmmountOfPairs(template):
    ammountEachPair = {}
    beginningPairs = [''.join(pair) for pair in zip(template[:-1], template[1:])]
    for pair in beginningPairs:
        if pair in ammountEachPair:
            ammountEachPair[pair] += 1
        else:
            ammountEachPair[pair] = 1
    return ammountEachPair

def BuildPolymer(allPairs, formula, steps, totalLetters, increases):
    step = 1
    newPairs = {}
    #print(allPairs)
    while step <= steps:
        print("building.....Step: ", step)
        for pair in allPairs.copy():
            #while there0s still pairs to evaluete (even if they are similar)
            multiplier = int(allPairs[pair])
            letterToIncrease = increases[pair]
            if letterToIncrease in totalLetters:
                totalLetters[letterToIncrease] += multiplier
            else:
                totalLetters[letterToIncrease] = multiplier
            for newPair in formula[pair]:
                if newPair in newPairs:
                    newPairs[newPair] += multiplier
                else:
                    newPairs[newPair] = multiplier
            allPairs[pair] -= 1
        allPairs = newPairs.copy()
        newPairs.clear()
        step += 1
    return totalLetters

def MostMinusLeast(totalLetters):
    MaxSingleLetter = 0
    MinSingleLetter = math.inf
    for key, number in totalLetters.items():
        #print(number)
        if number > MaxSingleLetter:
            MaxSingleLetter = number
        if number < MinSingleLetter:
            MinSingleLetter = number
    print (MaxSingleLetter - MinSingleLetter)

if __name__ == "__main__":
    main()
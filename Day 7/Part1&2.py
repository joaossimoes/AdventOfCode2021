

def main():
    input = open("input")
    #transform the data in {position:crabs at that position}
    dict, maxPos, minPos = OrganizeInput(input)
    CalculateFuelPart1(dict, maxPos, minPos)
    CalculateFuelPart2(dict, maxPos, minPos)

def OrganizeInput(input):
    dict = {}
    for line in input:
        crabs = list(map(int, line.strip().split(",")))

    maxPosition = max(crabs)
    minPosition = min(crabs)

    for position in crabs:
        if position in dict:
            dict[position] += 1
        else:
            dict[position] = 1
    return dict, maxPosition, minPosition

def CalculateFuelPart1(dict, maxPos, minPos):
    fuelSpent = 0
    minFuelSpent = 0
    position = 0
    for i in range(minPos, maxPos+1):
        fuelSpent = 0
        for key in dict:
            fuelSpent += (abs(i - key) )* dict[key]
        if i == minPos:
            minFuelSpent = fuelSpent
            position = i
        elif fuelSpent < minFuelSpent:
            minFuelSpent = fuelSpent
            position = i
    print ("Part 1: " , minFuelSpent, position)

def CalculateFuelPart2(dict, maxPos, minPos):
    fuelSpent = 0
    minFuelSpent = 0
    position = 0
    for i in range(minPos, maxPos+1):
        fuelSpent = 0
        for key in dict:
            fuelSpent += ((abs(i - key) * (abs(key-i) + 1))/2 ) * dict[key]
        if i == minPos:
            minFuelSpent = fuelSpent
            position = i
        elif fuelSpent < minFuelSpent:
            minFuelSpent = fuelSpent
            position = i
    print ("Part 2: ", minFuelSpent, position)

if __name__ == "__main__":
    main()
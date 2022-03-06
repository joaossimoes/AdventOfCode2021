
def main():
    steps = 1000
    input = treatInput()
    numberOfFlashes, step = Part1(input, steps)
    print(numberOfFlashes, step)

def treatInput():
    inputList = []
    rawInput = open("input")
    for line in rawInput:
        inputList.append(list(line.strip()))
    return inputList

def Part1(input, numbOfSteps):
    step = 1
    flashCoords = []
    numberOfFlashes = 0
    while step <= numbOfSteps:
        flashesPerStep = 0
        y = 0
        #APPLY + 1 MATH
        for line in input:
            x = 0
            for number in line:
                if int(number) == 9:
                    PreFlash(y, x, flashCoords)
                    numberOfFlashes += 1
                    flashesPerStep += 1
                    input[y][x] = 0
                    x += 1
                else:
                    input[y][x] = int(input[y][x]) + 1
                    x += 1
            y += 1
        

        #TODO: APPLY FLASHES
        while len(flashCoords) > 0:
            for flashX, flashY in flashCoords:
                adjacents = adjacent(flashY, flashX, input)
                for y, x in adjacents:
                    if int(input[y][x]) == 9 :
                        input[y][x] = 0
                        PreFlash(y, x, flashCoords)
                        numberOfFlashes += 1
                        flashesPerStep += 1
                    elif int(input[y][x]) == 0:
                        input[y][x] = 0
                    else:
                        input[y][x] = int(input[y][x]) + 1
                flashCoords.remove((flashX,flashY))

        if flashesPerStep == (len(input) * len(input[0])):
            print("They all flashed!")
            return flashesPerStep, step
        step += 1
    return numberOfFlashes, step

def PreFlash(x, y, flashes):
    flashes.append((x,y))

def adjacent(x, y, input):
    allAdjacents = [(1, 1), (1, 0), (1, -1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]
    adjacents = []
    for ya, xa in allAdjacents:
        if int(x+xa) >= 0 and int(x+xa) < len(input[x]) and int(y+ya) >= 0 and int(y+ya) < len(input):
            adjacents.append((y + ya, x + xa))
    return adjacents


if __name__ == "__main__":
    main()
import math
import time

def main():
    part2 = True
    input = TreatInput()
    if part2:
        print("treating input...")
        input = TreatInputPart2(input)
    startPos = (0, 0)
    endPos = (len(input[0]) - 1, len(input) - 1)

    
    origins = Dijkstra(input, startPos, endPos)
    path = BuildThePath(input, origins, endPos, startPos)
    CalculateRisk(input, path)

def TreatInputPart2(input):
    firstSize = len(input[0])
    for line in input:
        for number in line:
            if len(line) == firstSize * 5:
                break
            if number == 9:
                line.append(1)
            else:
                line.append(number + 1)
    
    for line in input:
        newLine = []
        
        if len(input) == firstSize * 5:
            break
        for number in line:
            if number == 9:
                newLine.append(1)
            else:
                newLine.append(number + 1)
        input.append(newLine.copy())

    return input

def TreatInput():
    input = []
    numbers = []
    rawInput = open("input")
    for line in rawInput:
        numbers = []
        for number in line.strip():
            numbers.append(int(number))
        input.append(numbers.copy())
    return input

def Dijkstra(input, startPos, endPos):
    start_time = time.time()
    finished = False

    distances = {}              #{(0,0) : 0}         pos: cost
    origins = {}                #{(0,1) : (0,0)}     endPos : starPos

    currentPos = startPos
    visited = []
    distancesStack = []

    #construnct a boolean list of visited points (all false at the beggining)
    for row in input:
        visitedCollums = []
        for collumn in row:
            visitedCollums.append(False)
        visited.append(visitedCollums.copy())
    
    #initial spot is visited
    x, y = startPos
    #visited[y][x] = True
    counter = 0
    while not finished:
        if counter % 10000 == 0:
            print("step: ", counter)
            print("--- %s seconds ---" % (time.time() - start_time))
            print("dict size: ", len(distances))
        distances, origins, distancesStack, visited = Explore(input, currentPos, distances, origins, distancesStack, visited)
        currentPos, visited = Move(distances, distancesStack, currentPos, visited)

        if currentPos == endPos:
            finished = True
        counter += 1
    
    return origins

def Explore(input, currentPos, distances, origins, distancesStack, visited):
    x, y = currentPos
    if (x, y) in distances:
        cost = distances[(x, y)]
        del distances[(x,y)]
    else:
        cost = 0
    
  
    if x > 0:
        if visited[y][x-1] == False:
            if (x-1, y) not in distances:
                distances[(x-1,y)] = input[y][x-1] + cost
                distancesStack.append(input[y][x-1] + cost)
                origins[(x-1,y)] = currentPos

            elif distances[(x-1,y)] > input[y][x-1] + cost:
                distances[(x-1,y)] = input[y][x-1] + cost
                distancesStack.append(input[y][x-1] + cost)
                origins[(x-1,y)] = currentPos

    if x < len(input[0]) - 1:
        if visited[y][x+1] == False:
            if (x+1, y) not in distances:
                distances[(x+1,y)] = input[y][x+1] + cost
                distancesStack.append(input[y][x+1] + cost)
                origins[(x+1,y)] = currentPos

            elif distances[(x+1,y)] > input[y][x+1] + cost:
                distances[(x+1,y)] = input[y][x+1] + cost
                distancesStack.append(input[y][x+1] + cost)
                origins[(x-1,y)] = currentPos
    
    if y > 0:
        if visited[y-1][x] == False:
            if (x, y-1) not in distances:
                distances[(x,y-1)] = input[y-1][x] + cost
                distancesStack.append(input[y-1][x] + cost)
                origins[(x,y-1)] = currentPos

            elif distances[(x,y-1)] > input[y-1][x] + cost:
                distances[(x,y-1)] = input[y-1][x] + cost
                distancesStack.append(input[y-1][x] + cost)
                origins[(x-1,y)] = currentPos

    if y < len(input) - 1:
        if visited[y+1][x] == False:
            if (x, y+1) not in distances:
                distances[(x,y+1)]  = input[y+1][x] + cost
                distancesStack.append(input[y+1][x] + cost)
                origins[(x,y+1)] = currentPos

            elif distances[(x,y+1)] > input[y+1][x] + cost:
                distances[(x,y+1)] = input[y+1][x] + cost
                distancesStack.append(input[y+1][x] + cost)
                origins[(x-1,y)] = currentPos
    
    distancesStack.sort()
    distancesStack = list(dict.fromkeys(distancesStack))
    return distances, origins, distancesStack, visited


def Move(distances, distancesStack, currentPos, visited):

    for i in range(len(distancesStack)):
        for key,value in distances.items():
            if value == distancesStack[i]:
                x , y = key
                if visited[y][x] == False:
                    visited[y][x] = True
                    currentPos = key
                    if i > 0:
                        for j in range(0,i):
                            distancesStack.pop(0)
                    return currentPos, visited

def BuildThePath(input, origins, endPos, startPos):
    afterPos = endPos
    originalPos = startPos
    path = []
    while True:
        if afterPos in origins:
            path.append(afterPos)
            afterPos = origins[afterPos]

        if afterPos == originalPos:
            return path
    
def CalculateRisk(input, path):
    risk = 0
    for x, y in path:
        risk += int(input[y][x])
    print(risk)


if __name__ == "__main__":
    main()
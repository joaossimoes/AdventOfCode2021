
#TODO: THIS CODE HAS A VERY BIG OTIMIZATION PROBLEM

def main():
    timesToFold = 12
    paper, folds, maxX, maxY = BuildPaper()
    foldedPaper = Fold(paper, timesToFold, folds, maxX, maxY)
    #print(foldedPaper)
    part1 = CountDots(foldedPaper)
    print(part1)
    BuildString(foldedPaper)



def BuildPaper():
    rawInput = open("input")
    points = []
    folds = []
    maxX = 0
    maxY = 0
    for line in rawInput:
        if line.startswith("fold"):
            words, number = line.strip().split("=")
            if "y" in words:
                folds.append(("y", number))
            if "x" in words:
                folds.append(("x", number))
        elif line.strip() != "":
            x, y = line.strip().split(",")
            points.append((x, y))
            if int(x) > int(maxX):
                maxX = x
            if int(y) > int(maxY):
                maxY = y
    rawPaper = BuildDict(maxX, maxY)

    for (x, y) in points:
        if (int(x), int(y)) in rawPaper:
            rawPaper[(int(x), int(y))] = "#"
    return rawPaper, folds, maxX, maxY

def Fold(paper, timesToFold, folds, maxX, maxY):
    fold = 0
    while fold < timesToFold:
        axis, number = folds[fold]
        #fold on Y axis
        if axis == "y":
            start = int(number) - 1
            end = int(number) + 1
            for (x, y) in paper.copy():
                if y == int(number):
                    del paper[x, int(number)]

            for (x, y) in paper.copy():
                if paper[(x, y)] == "#":
                    if int(y) > int(number):
                        opposite = y - int(number)
                        paper[(x, int(number) - opposite)] = "#"
                if int(y) > int(number):
                    del paper[(x, y)]
        
        if axis == "x":
            start = int(number) - 1
            end = int(number) + 1
            for (x, y) in paper.copy():
                if x == int(number):
                    del paper[int(number), y]

            for (x, y) in paper.copy():
                if paper[(x, y)] == "#":
                    if int(x) > int(number):
                        opposite = x - int(number)
                        paper[int(number) - opposite, y] = "#"
                if int(x) > int(number):
                    del paper[(x, y)]
        fold += 1
    return paper


def CountDots(foldedPaper):
    counter = 0
    for (x ,y) in foldedPaper:
        if foldedPaper[(x, y)] == "#":
            counter += 1
    return counter

def BuildDict(maxX, maxY):
    paper = {}
    y = 0
    x = 0
    while y <= int(maxY):
        x = 0
        while x <= int(maxX):
            paper[(x,y)] = "."
            x += 1
        y += 1
    return paper

def BuildString(foldedPaper):
    string = ""
    print(foldedPaper)
    for (x, y) in foldedPaper:
        if x == 0:
            print("")
        print(str(foldedPaper[(x,y)]), end = "")
    

if __name__ == "__main__":
    main()
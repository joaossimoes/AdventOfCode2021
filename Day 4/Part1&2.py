import re

def main():
    minRound = 100
    maxRound = 0
    minCardList = []
    maxCardList = []
    somaMin = 0
    somaMax = 0
    draw = TakeDraw()
    i = 0
    cardThatWonFirst = 0
    cardThatWonLast = 0
    while i <= 99:
        cardToAnalize, cardList = BuildCard(i)
        round, cardListAfterWin = CheckForWin(draw, cardToAnalize, cardList)
        if round < minRound:
            minRound = round
            minCardList = cardListAfterWin.copy()
            cardThatWonFirst = i
        if round > maxRound:
            maxRound = round
            maxCardList = cardListAfterWin.copy()
            cardThatWonLast = i
        i += 1
    for number in minCardList:
        somaMin += int(number)
    for number in maxCardList:
        somaMax += int(number)
    print("Result part 1: " ,somaMin * int(draw[minRound]))
    print("Result part 2: ", somaMax * int(draw[maxRound]))
    

#TODO: FOR EACH CARD CHECK THE ROUND WHERE THE WIN CONDITION IS MET AND STORE A LIST OF NOT MARKED NUMBERS. COMPARED WIN ROUNDS EVERYTIME WE CHECK A CARD AND STORE ONLY THE LIST
#AND ROUND OF THE ONE THAT HAS THE SMALEST ROUND

def TakeDraw():
    with open("input") as f:
        firstLine = f.readline()
    drawList = firstLine.split(",")
    return drawList

def BuildCard(cardNumber):
    input = open("input")
    card = []
    numberCardList = []
    i = 2
    counter = 0
    lineToStart = i + (6 * cardNumber)
    lines = input.readlines()
    while counter < 5:
        row = re.split(r"\s+", lines[lineToStart + counter].strip())
        card.append(row)
        for number in row:
            numberCardList.append(number)
        counter += 1
    return card, numberCardList

def CheckForWin(draw, cardToAnalize, cardList):
    round = 0
    column = 0
    row = 0
    marksDictionary = {}
    for round in range(len(draw)):
        row = 0
        while row < 5:
            column = 0
            while column < 5:
                if draw[round] == cardToAnalize[row][column]:
                    cardList.remove(draw[round])
                    marksDictionary[column, row] = "1"
                column += 1
            row += 1
        if CheckIfBingo(marksDictionary):
            return round, cardList

def CheckIfBingo(marksDictionary):
    row = 0
    collumn = 0
    countForBingoH = 0
    while collumn < 5:
        if (row, collumn) in marksDictionary:
            countForBingoH += 1
            row += 1
            if countForBingoH == 5:
                return True
        else:
            collumn += 1
            row = 0
            countForBingoH = 0
    
    row = 0
    collumn = 0
    countForBingoV = 0
    while row < 5:
        if (row, collumn) in marksDictionary:
            countForBingoV += 1
            collumn += 1
            if countForBingoV == 5:
                return True
        else:
            row += 1
            collumn = 0
            countForBingoV = 0
    return False

if __name__ == "__main__":
    main()
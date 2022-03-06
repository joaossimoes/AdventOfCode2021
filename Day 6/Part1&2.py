from typing import Mapping


def main():
    input = open("input")
    maxTimer = 6
    timerAfterBirth = maxTimer + 2
    days = 256
    fishes = BuildDict(input)
    print(fishes)
    fishesAfterTime = PassTheDays(fishes, days, maxTimer, timerAfterBirth)
    CountFishes(fishesAfterTime)


def BuildDict(input):
    dict = {}
    for line in input:
        line = line.split(",")
    for number in line:
        if int(number) in dict:
            dict[int(number)] += 1
        else:
            dict[int(number)] = 1
    return dict

def PassTheDays(dict, days, maxTimer , timeAfterBirth):
    newDict = {}
    actualDay = 1
    i = 0
    while actualDay <= days:
        counter = timeAfterBirth
        while counter >= 0:
            if counter == 0:
                if counter in dict:
                    if maxTimer in newDict:
                        newDict[maxTimer] += dict[counter]
                    else:
                        newDict[maxTimer] = dict[counter]
                    newDict[timeAfterBirth] = dict[counter]

            elif counter in dict:
                newDict[int(counter) - 1] = dict[counter]
            counter -= 1
        dict = newDict.copy()
        newDict = {}
        actualDay += 1
    return dict

def CountFishes(dict):
    result = 0
    for key in dict.keys():
        result += dict[key]
    print(result)

if __name__ == "__main__":
    main()
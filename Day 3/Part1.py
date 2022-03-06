
def GetInputList():
    input = open("input")

    lista = []

    for number in input:
        number = number.strip('\n')
        lista.append(number)
    return lista

def BuildDictionary(input):
    dict = {}
    for number in input:
        posCount = 0
        for i in number:
            if i == '0':
                #check if the bit is zero, if it is add a counter to his position in the dictionary (dic = {position : counter})
                if posCount in dict:
                    dict[posCount] += 1
                else:
                    dict[posCount] = 1
            posCount += 1
    return dict

def BuildGamma(dict, inputSize):
    gamma = ""
    epsilon = ""
    i = 0
    #Go through dictionay and fiding the most popular bit value for each position
    while i < len(dict):
        if dict[i] > inputSize/2:
            gamma += "0"             #gamma and epsilon are opposites bit wise
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
        i += 1
    return gamma, epsilon

def DoTheMath(gamma, epsilon):
    #get result in decimal value
    result = int(gamma, 2) * int(epsilon, 2) 
    return result

def main():
    #put the input in list form
    input = GetInputList()                     
    inputSize = len(input)
    #create a dictionary where = {Position : number of zeros in Position}
    dict = BuildDictionary(input)
    print(dict)               
    #Get gamma and epsilon values
    gamma, epsilon = BuildGamma(dict, inputSize)
    #Get result
    result = DoTheMath(gamma, epsilon)
    print(result)
    

if __name__ == "__main__":
    main()
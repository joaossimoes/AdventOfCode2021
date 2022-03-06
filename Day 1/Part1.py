f = open("inputP1")

count = 0
numb1 = 0
numb2 = 0
firstTime = True
for line in f:
    numb1 = int(line)
    if numb1 > numb2:
        count+=1
        if firstTime:
            count = 0
            firstTime = False
    numb2 = numb1
print(count)
    
        
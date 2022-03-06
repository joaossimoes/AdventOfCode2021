import time
start_time = time.time()
input = open("InputD2")

direction = ""
move = 0

hPos = 0
depth = 0
aim = 0

result = 0


for line in input:
    direction, move = line.split(" ")
    if direction == "forward":
        hPos += int(move)
        depth += (aim * int(move))
    elif direction == "down":
        aim += int(move)
    else:
        aim -= int(move)

result = hPos * depth

print(result)
print("--- %s seconds ---" % (time.time() - start_time))
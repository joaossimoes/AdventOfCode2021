input = open("InputD2")

direction = ""
move = 0

hPos = 0
depth = 0

result = 0

for line in input:
    direction, move = line.split(" ")
    if direction == "forward":
        hPos += int(move)
    elif direction == "down":
        depth += int(move)
    elif direction == "up":
        depth -= int(move)

result = hPos * depth

print(result)
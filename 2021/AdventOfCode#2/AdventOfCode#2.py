lines = []
with open('AdventOfCode#2\Input.txt') as f:
    lines = f.readlines()

PosHorizontal = 0
PosDepth = 0
Aim = 0

for line in lines:
    temp = line.split()
    if(temp[0] == "forward"):
        PosHorizontal += int(temp[1])
        PosDepth += Aim * int(temp[1])
    elif temp[0] == "down":
        Aim += int(temp[1])
    else:
        Aim -= int(temp[1])
    
print(str(PosHorizontal) + " " + str(PosDepth) + ": " + str(PosHorizontal * PosDepth))
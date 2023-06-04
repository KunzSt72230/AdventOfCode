lines = []
with open('AdventOfCode#13\Input.txt') as f:
    lines = f.readlines()

coords =[]
instructions = []
for coord in lines:
    coord = coord.strip("\n")
    if coord.__contains__("fold"):
        instructions.append(coord)
    else:
        coord = coord.split(',')
        if coord != ['']:
            coord[0] = int(coord[0])
            coord[1] = int(coord[1])
            coords.append(coord)

for instruction in instructions:
    instruction = instruction.replace('fold along ', '')
    direction = instruction[0]
    weight = instruction[2:]

#print(coords)

xCoords = []
yCoords = []
for item in coords:
    xCoords.append(item[0])
    yCoords.append(item[1])
xCoords.sort()
xSize = xCoords[-1]
yCoords.sort()
ySize = yCoords[-1]
tempXY = [0,0]

newPoint = [0,0]
foldCounter = 0

for instruction in instructions: #First empty instruction, then real instructions
    instruction = instruction.replace('fold along ', '')
    direction = instruction[0]
    weight = int(instruction[2:])
    print()
    print("After " + str(foldCounter) + " folds!")
    NumberOfPoints = len(coords)

    for row in range(ySize + 1):
        for column in range(xSize + 1):
            tempXY[0] = column
            tempXY[1] = row
            newPoint = [0,0]

            #Draw the board
            if foldCounter == len(instructions) -1 :
                if tempXY in coords:
                    print("#", end="")
                elif row == weight and direction == 'y':
                    print('_', end='')
                elif column == weight and direction == 'x':
                    print('|', end='')
                else:
                    print(".", end="")
       
            if direction == 'y':
                if row > weight and tempXY in coords:
                    newPoint[0] = column
                    newPoint[1] = row - 2*(row - weight)
                    coords.remove(tempXY)
                    if not(newPoint in coords):
                        coords.append(newPoint)
            else:
                if column > weight and tempXY in coords:
                    newPoint[0] = column - 2*(column - weight)
                    newPoint[1] = row
                    coords.remove(tempXY)
                    if not(newPoint in coords):
                        coords.append(newPoint)

        if foldCounter == len(instructions) -1 :
            print()
        
    print("Number of Points: " + str(NumberOfPoints))
    if direction == 'y':
        ySize = int(ySize / 2) -1
    else:
        xSize = int(xSize / 2) -1
    
    foldCounter = foldCounter + 1

    # if foldCounter == 2:
    #     break

help = 0

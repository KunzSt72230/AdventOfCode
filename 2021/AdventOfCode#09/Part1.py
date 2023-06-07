lines = []
with open('2021\AdventOfCode#9\InputTest.txt') as f:
    lines = f.readlines()

board = [ [0]*(len(lines[0])-1) for i in range(0, len(lines))]
for row in range(0, len(lines)):
    for column in range(0, len(lines[0])-1):
        board[row][column] = int(lines[row][column])

#print(board)

lowpoints = []

for row in range(0, len(board)):
    for column in range(0, len(board[row])):

        center = board[row][column]

        if(row == 0):
            up = 9
        else:
            up = board[row-1][column]
        if(row == len(board)-1):
            down = 9
        else:
            down = board[row+1][column]
        if(column == 0):
            left = 9
        else:
            left = board[row][column-1]
        if(column == len(board[row])-1):
            right = 9
        else:
            right = board[row][column+1]

        if not(center > up or center > down or center > left or center > right or center == 9):
            lowpoints.append(center)

print(lowpoints)

result = 0
for x in lowpoints:
    x += 1
    result += x

print("Das Resultat ist: " + str(result))


                



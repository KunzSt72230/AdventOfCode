input = []
test = []
boards = []
with open('AdventOfCode#4\InputTest.txt') as f:
    input = f.readline().strip()
    boards = f.read()[0:].split()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class BingoBoard:
    def __init__(self, board):
        self.board = board

    def MarkedNumber(number):
        pass
    
    def DrawBoard(self):
        start = 0
        end = 5
        for y in range(0,5):
            for x in range(start,end):
                if self.board[x] < 10: 
                    print(" " + str(self.board[x]) + " ", end='')
                else:
                    print(str(self.board[x]) + " ", end='')
            print()
            start += 5
            end += 5
        print()


    def Hello(abc):
        print("Hello")


print(bcolors.HEADER + "Beginning of Programm" + bcolors.ENDC)

List = []
start = 0
end = 25
temp = [0] * 25
while end <= len(boards):
    for x in range(0, 25):
        temp[x] = int(boards[x + start])
    List.append(BingoBoard(temp))
    start += 25
    end += 25
    temp = [0] * 25

print(input)
for obj in List:
    obj.DrawBoard()



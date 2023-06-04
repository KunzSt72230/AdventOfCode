lines = []
with open('AdventOfCode#10\Input.txt') as f:
    lines = f.readlines()

RKlammer = 0
GKlammer = 0
EKlammer = 0
SKlammer = 0
Klammern = []
score = []
pop = ''
illegalFound = False
list = []

for line in lines:
    for char in line.strip():
        if (illegalFound == False):
                
            if char == '(':
                RKlammer += 1
                Klammern.append(char)
            elif char == ')':
                if Klammern[-1] == '(':
                    RKlammer -= 1
                    pop = Klammern.pop()
                else:
                    illegalChar = char
                    illegalFound = True
            elif char == '{':
                GKlammer += 1
                Klammern.append(char)
            elif char == '}':
                if Klammern[-1] == '{':
                    GKlammer -= 1
                    pop = Klammern.pop()
                else: 
                    illegalChar = char
                    illegalFound = True
            elif char == '[':
                EKlammer += 1
                Klammern.append(char)
            elif char == ']':
                if Klammern[-1] == '[':
                    EKlammer -= 1
                    pop = Klammern.pop()
                else: 
                    illegalChar = char
                    illegalFound = True
            elif char == '<':
                SKlammer += 1
                Klammern.append(char)
            elif char == '>':
                if Klammern[-1] == '<':
                    SKlammer -= 1
                    pop = Klammern.pop()
                else: 
                    illegalChar = char
                    illegalFound = True
            else: illegalFound = True    
              
        if illegalFound == True: break

    if illegalFound == False:
        print(f"ALLES OK: ", line, end = '')
        print(Klammern)
        newKlammern = Klammern[::-1]
        list.append(newKlammern)


    pop = ''
    Klammern = []
    RKlammer = 0
    GKlammer = 0
    EKlammer = 0
    SKlammer = 0
    illegalFound = False
    illegalChar = ""

for x in list:
    print(x)
    subScore = 0
    for y in x:
        subScore *= 5
        if y == '(':
            subScore += 1
        elif y == '[':
            subScore += 2
        elif y == '{':
            subScore += 3
        elif y == '<':
            subScore += 4
    score.append(subScore)
    
score.sort()

print(score[int((len(score)-1) / 2)])



lines = []
with open('AdventOfCode#10\Input.txt') as f:
    lines = f.readlines()

RKlammer = 0
GKlammer = 0
EKlammer = 0
SKlammer = 0
Klammern = []
score = 0
pop = ''
illegalFound = False
counter = 1

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
        #print(line)
        #print("ALLES OK")
        temp = 0
    else:
        
        expectedChar = ''
        pop = Klammern.pop()
        if pop == '(':
            expectedChar = ')'
        elif pop == '{':
            expectedChar = '}'
        elif pop == '[':
            expectedChar = ']'
        elif pop == '<':
            expectedChar = '>'

        #print("ILLEGAL CHARACTER FOUND")
        print("Expected: '" + expectedChar + "' But found : '" + illegalChar + "'")
        #print(line)        
        if illegalChar == ')':
            score += 3
        elif illegalChar == ']':
            score += 57
        elif illegalChar == '}':
            score += 1197
        elif illegalChar == '>':
            score += 25137

    pop = ''
    Klammern = []
    RKlammer = 0
    GKlammer = 0
    EKlammer = 0
    SKlammer = 0
    illegalFound = False
    illegalChar = ""
    #print(counter)
    counter += 1
        
print(score)


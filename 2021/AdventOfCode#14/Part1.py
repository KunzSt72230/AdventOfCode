polymereTemplate = []
lines = []
with open('2021\AdventOfCode#14\InputTest.txt') as f:
    polymereTemplate = f.readline().strip()
    lines = [line.strip() for line in f if line.strip()]


instructions = dict()
for line in lines:
    key = line[0:2] 
    value = line[6]
    instructions[key] = value

print("After step 0: " + polymereTemplate)
for step in range(1, 41):
    newTemplate = []
    for x in range(len(polymereTemplate) - 1):
        pair = polymereTemplate[x:x+2]
        newTemplate += pair[0] + instructions[pair] 
    
    newTemplate += pair[1]
    #print("After step " + str(step) + ": " + "".join(newTemplate))
    polymereTemplate = "".join(newTemplate)

letterMap = []
string = "".join(newTemplate)
for char in string:
    letterMap.append(string.count(char))
    string.replace(char, '')

letterMap.sort()
MostCommonLetter = letterMap[-1]
LeastCommonLetter = letterMap[0]
result = MostCommonLetter - LeastCommonLetter
print(result)
lines = []
with open('AdventOfCode#3\Input.txt') as f:
    lines = f.readlines()


def Split(line):
    return [x for x in line]

# gammaRate = ""
# epsilonRate = ""
# oneCounter = 0
# zeroCounter = 0

# for x in range(0, len(lines[0])-1):
#     for line in lines:
#         temp = Split(line)
#         if temp[x] == "0":
#             zeroCounter += 1
#         else:
#             oneCounter += 1

#     if zeroCounter > oneCounter:
#         gammaRate = gammaRate + "0"
#         epsilonRate = epsilonRate + "1"
#     else:
#         gammaRate = gammaRate + "1"
#         epsilonRate = epsilonRate + "0"
#     zeroCounter = 0
#     oneCounter = 0

# print("The GammaRate is   : " + (str(gammaRate)))
# print("The EpsilonRate is : " + (str(epsilonRate)))
# gammaDezimal = 0
# epsilonDezimal = 0
# for Digit in gammaRate:
#     gammaDezimal = gammaDezimal*2 + int(Digit)
# for Digit in epsilonRate:
#     epsilonDezimal = epsilonDezimal*2 + int(Digit)
# print(gammaDezimal)
# print(epsilonDezimal)
# print("Ergebnis: " + str(epsilonDezimal * gammaDezimal)) 

#-----Aufgabe 3.2-------
newlines = []
columnArray = []

def OxGenerator(array):
    oneCounter = 0
    zeroCounter = 0

    for x in array:
        if x == "0":
            zeroCounter += 1
        else:
            oneCounter += 1

    if oneCounter >= zeroCounter:
        return 1
    else:
        return 0        

for x in range(0, len(lines[0])-1): 
    
    for line in lines:
        temp = Split(line)
        #print(temp[x])
        columnArray.append(temp[x])

    bitvalue = OxGenerator(columnArray)
    for line in lines:
        temp = Split(line)
        if int(temp[x]) == bitvalue:
            newlines.append(line)
    

    #for i in range(0, len(newlines)):
        #print(newlines[i], end = "")
    
    #print("\n------------")
    
    if len(newlines) == 1:
        break
   
    lines = newlines
    newlines = []
    columnArray = []

OxygenRating = newlines[0]
OxygenRating = OxygenRating[: -1]
print("OxygenRating is: " + OxygenRating)
OxDezimal = 0
for Digit in OxygenRating:
    OxDezimal = OxDezimal*2 + int(Digit)
print(OxDezimal)

#----------------------------------------------

with open('AdventOfCode#3\Input.txt') as f:
    lines = f.readlines()

newlines = []
columnArray = []     

def C02Scrubber(array):
    oneCounter = 0
    zeroCounter = 0

    for x in array:
        if x == "0":
            zeroCounter += 1
        else:
            oneCounter += 1

    if zeroCounter <= oneCounter:
        return 0
    else:
        return 1        

for x in range(0, len(lines[0])-1): 
    
    for line in lines:
        temp = Split(line)
        #print(temp[x])
        columnArray.append(temp[x])

    bitvalue = C02Scrubber(columnArray)
    for line in lines:
        temp = Split(line)
        if int(temp[x]) == bitvalue:
            newlines.append(line)
    

    for i in range(0, len(newlines)):
        print(newlines[i], end = "")
    
    print("\n------------")
    
    if len(newlines) == 1:
        break
   
    lines = newlines
    newlines = []
    columnArray = []

C02Rating = newlines[0]
C02Rating = C02Rating[: -1]
print("C02Rating is: " + C02Rating)
C02Dezimal = 0
for Digit in C02Rating:
    C02Dezimal = C02Dezimal*2 + int(Digit)
print(C02Dezimal)
print("Ergebnis: " + str(OxDezimal * C02Dezimal))
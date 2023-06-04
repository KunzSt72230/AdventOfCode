lines = []
with open('AdventOfCode#1\Input.txt') as f:
    lines = f.readlines()
#Aufgabe 1.1

"""
count = 0
previousLine = 0
value = ""
for line in lines:
    if previousLine == 0:
        value = " N/A -- no available measurment"
    elif int(line) > previousLine:
        value = "increased"
        count += 1
    else:
        value = "decreased"
    #print(str(line).strip() + " " + value)
    previousLine = int(line)

print("The Value increased: " + str(count) + " times") """

#Aufgabe 1.2
sum = 0
previousSum = 0
counter = 0
count = 0
value = ""
for line in lines[0: len(lines)-2]:
    sum = int(lines[counter]) + int(lines[counter + 1]) + int(lines[counter+2])
    if previousSum == 0:
        value = " N/A -- no available measurment"
    elif sum > previousSum:
        value = " increased"
        count += 1
    else:
        value = " decreased"

    #print(str(sum) + " " + str(previousSum) +value)
    previousSum = sum
    counter += 1

print("The Value increased: " + str(count) + " times") 
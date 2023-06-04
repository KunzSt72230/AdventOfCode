import math

lines = []
with open('AdventOfCode#7\Input.txt') as f:
    lines = f.read().split(',')

median = 0
crab = []

for x in lines:
    crab.append(int(x))
#crab.sort()
#print(crab)

average = 0
for x in crab:
    average += x


average = int((average / len(crab)))


print("Mittelwert ist : " + str(average))
fuelTotal = 0

for x in crab:
    fuelConsumption = 0
    distance = abs(x-average)
    for x in range(0, distance + 1):
        fuelConsumption += x 
    #print(distance, end= ', ')
    #print(fuelConsumption)
    fuelTotal += fuelConsumption

print("Gesamtverbrauch ist : " + str(fuelTotal))
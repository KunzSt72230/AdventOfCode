lines = []
with open('2021\AdventOfCode#7\Input.txt') as f:
    lines = f.read().split(',')

median = 0
crab = []

for x in lines:
    crab.append(int(x))
crab.sort()

median = crab[int(len(crab) / 2)]
print("Median ist : " + str(median))
fuelTotal = 0

for x in crab:
    fuelTotal += abs(x-median)
print("Gesamtverbrauch ist : " + str(fuelTotal))

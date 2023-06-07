lines = []
with open('AdventOfCode#6\InputTest.txt') as f:
    lines = f.read()

day = 1

print("Initial state: " + str(lines))
fish = []
for value in lines:
    if value is not ',':
        temp = int(value)
        fish.append(temp)

while day <= 80:
    for i in range(len(fish)):
        if fish[i] == 0:
            fish.append(8)
            fish[i] = 7
        fish[i] = fish[i] - 1
    day += 1
    
    #print("After   " + str(day) + " day: ", end='')
    #print(*fish, sep=',')

print("The Number of Lanternfish are: " + str(len(fish)))
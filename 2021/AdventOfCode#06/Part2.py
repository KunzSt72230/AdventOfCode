lines = []
with open('2021\AdventOfCode#6\Input.txt') as f:
    lines = f.read()

day = 1
map = [0] * 9

fish = []
score = 0
for value in lines:
    if value is not ',':
        temp = int(value)
        fish.append(temp)

for x in fish:
    map[x] += 1

print("Initial state: " + str(map))
saved6 = 0
saved8 = 0

while day <= 256:
    for x in range(len(map)):
        if x == 0:
            saved8 = map[0]
            saved6 = map[0]
            map[0] = 0
        else:
            map[x-1] += map[x]
            map[x] = 0
    map[6] += saved6
    map[8] += saved8
    print("After " + str(day) + "   day: ", end='')
    print(*map, sep=',')
    day += 1

score = 0
for x in map:
    score += x

print("The Number of Lanternfish are: " + str(score))
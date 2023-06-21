import collections

polymere = []
lines = []
with open('2021\AdventOfCode#14\Input.txt') as f:
    polymere = f.readline().strip()
    lines = [line.strip() for line in f if line.strip()]


instructions = {}
counter = collections.Counter()
for line in lines:
    src, dst = line.split(' -> ')
    instructions[src] = dst
    #counter[src] = 0

#print(instructions)
for i in range(0, len(polymere)-1): 
    counter[polymere[i:i+2]] += 1

#print(counter)
for i in range(40):
    new_counter = collections.Counter()
    char_counter = collections.Counter()
    for x,y in counter.items():
        new_counter[f'{x[0]}{instructions[x]}'] += y
        new_counter[f'{instructions[x]}{x[1]}'] += y
        char_counter[x[0]] += y
        char_counter[instructions[x]] += y
    counter = new_counter

char_counter[polymere[-1]] += 1
values = sorted(char_counter.values())
print(values[-1] - values[0])
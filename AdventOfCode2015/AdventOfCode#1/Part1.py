input = []
with open('AdventOfCode2015\AdventOfCode#1\Input.txt') as f:
    input = f.readline().strip()

score = 0
counter = 0
for c in input:
    if c == '(':
        score += 1
        counter += 1
    else:
        score -= 1
        counter += 1
    if score == -1:
        print(counter)

print(score)

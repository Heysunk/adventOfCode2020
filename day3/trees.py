
input_lines = []
with open("input.txt") as file_in:
    for line in file_in:
        input_lines.append(line)
xSize = len(input_lines[0]) - 1
ySize = len(input_lines)
x = 0
y = 0

treesHit = 0
yMove = 1
xMove = 3
while(y < ySize):
    if (input_lines[y][x] == '#'):
        treesHit += 1
    x = (xMove + x) % xSize
    y += yMove

print(treesHit)




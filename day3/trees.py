


def calcHitTrees(input_lines, yMove, xMove):

    xSize = len(input_lines[0]) - 1
    ySize = len(input_lines)
    x = 0
    y = 0

    treesHit = 0
    while(y < ySize):
        if (input_lines[y][x] == '#'):
            treesHit += 1
        x = (xMove + x) % xSize
        y += yMove

    return treesHit




input_lines = []
with open("input.txt") as file_in:
    for line in file_in:
        input_lines.append(line)

prod = calcHitTrees(input_lines, 1,1)
prod *= calcHitTrees(input_lines, 1,3)
prod *= calcHitTrees(input_lines, 1,5)
prod *= calcHitTrees(input_lines, 1,7)
prod *= calcHitTrees(input_lines, 2,1)

print(prod)

import math
import re



validBpassRegex = re.compile('^[FB]{7}[RL]{3}$')

def narrowLoc(lower, upper, tightenTowardsUpper):
    size = upper - lower
    newSize = size/2.0
    newSize = math.ceil(newSize)
    if tightenTowardsUpper:
        lower = int(lower + newSize)
    else:
        upper = int(upper - newSize)
    return (lower, upper)


def determineSeatID(bpass):
    lowerRow = 0
    upperRow = 127
    lowerCol = 0
    upperCol = 7
    for char in bpass:
        if char == 'F':
            lowerRow, upperRow = narrowLoc(lowerRow, upperRow, False)
        elif char == 'B':
            lowerRow, upperRow = narrowLoc(lowerRow, upperRow, True)
        elif char == 'R':
            lowerCol, upperCol = narrowLoc(lowerCol, upperCol, True)
        elif char == 'L':
            lowerCol, upperCol = narrowLoc(lowerCol, upperCol, False)
        else:
            raise AssertionError('Invalid token in bpass: ' + char)
    if not lowerRow == upperRow:
        raise AssertionError("lowerRow does not equal upperRow: " + str(lowerRow) + ", upper: " + str(upperRow))
    if not lowerCol == upperCol:
        raise AssertionError("lowerCol does not equal upperCol: " + str(lowerCol) + ", upper: " + str(upperCol))

    #Calc seatID
    return lowerRow * 8 + lowerCol



bpasses = []
with open("input.txt") as file_in:
    for line in file_in:
        line = line.strip()
        if not validBpassRegex.match(line):
            raise AssertionError("input data contains invalid bpass: " + line)
        bpasses.append(line)


highestSeatID = 0
for bpass in bpasses:
    seatID = determineSeatID(bpass)
    if seatID > highestSeatID:
        highestSeatID = seatID


print(highestSeatID)

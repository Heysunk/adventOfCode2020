import copy
# create data structure with neighbours (the adapters that can be reached from this one)
# solve recursively bottom up, so we always pass the highest value from the previous one, and multiply it by the amount of neighbours

#assume already sorted

# 0 signifies the floor, 1 signifies an empty seat, and 2 is a occupied seat
# The seatMatrix contains an empty row and an empty column in the last index of y/x, this simplies newSeatStateCalc
def allocateSeats(seatMatrix):
    yLen = len(seatMatrix) -1
    xLen = len(seatMatrix[0]) -1
    newSeatMatrix = copy.deepcopy(seatMatrix)
    stateChange = False
    for i in range(0, yLen):
        for j in range(0, xLen):
            newValue =  newSeatState(seatMatrix, i,j)
            if newValue != seatMatrix[i][j]:
                stateChange = True
            newSeatMatrix[i][j] = newValue

    return (newSeatMatrix, stateChange)

def countOccupiedSeats(seatMatrix):
    count = 0
    for row in seatMatrix:
        for seat in row:
            if seat == 2:
                count += 1
    return count
def newSeatState(seatMatrix, y, x):
    yLen = len(seatMatrix)
    xLen = len(seatMatrix[0])

    # Seat is empty
    if y == yLen - 1 or x == xLen - 1 or seatMatrix[y][x] == 0:
        # The seat is a part of the virtual bounds which only exist to simplify calculations
        return 0
    occupiedCount = 0
    for i in range (-1, 2):
        for j in range (-1, 2):
            if i == 0 and j == 0:
                continue
            boundedY = (y + i) % yLen
            boundedX = (x + j) % xLen
            if seatMatrix[boundedY][boundedX] == 2:
                occupiedCount += 1
    if seatMatrix[y][x] == 2:
        if occupiedCount >= 4:
            return 1
        else:
            return 2
    elif seatMatrix[y][x] == 1:
        if occupiedCount == 0:
            return 2
        else:
            return 1

def printSeatMatrix(seatMatrix):
    yLen = len(seatMatrix) -1
    xLen = len(seatMatrix[0]) -1
    for i in range(0, yLen):
        s = ""
        for j in range(0, xLen):
            seat = seatMatrix[i][j]
            if seat == 0:
                s = s + '.'
            if seat == 1:
                s = s + 'L'
            if seat == 2:
                s = s + '#'

        print(s)
    print()

seatMatrix = []
with open("input.txt") as file_in:
    for line in file_in:
        seatCol = []
        line = (line.rstrip())
        for char in line:
            if char == '.':
                seatCol.append(0)
            if char == 'L':
                seatCol.append(1)
            if char == '#':
                seatCol.append(2)
        # Add virtual collumn to simplify calculations
        seatCol.append(0)

        seatMatrix.append(seatCol)
    # add row with same length with 0
    xLen = len(seatMatrix[0])
    virtualRow = []
    for i in range(0, xLen):
        virtualRow.append(0)
    seatMatrix.append(virtualRow)
stateChange = True
while stateChange:
    seatMatrix, stateChange = allocateSeats(seatMatrix)
    #printSeatMatrix(seatMatrix)

print (countOccupiedSeats(seatMatrix))


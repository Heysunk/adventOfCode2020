


def determineValidNumber(rollingList, num):
    for x in rollingList:
        for y in rollingList:
            if x + y == num:
                return True
    return False


def findContiguousInterval(inputList, numToFind):
    startIndex = 0

    while startIndex < len(inputList):
        totSum = 0
        i = startIndex
        smallestNum = 10000000000000000
        largestNum = -1
        while i < len(inputList):
            totSum += inputList[i]
            if inputList[i] < smallestNum:
                smallestNum = inputList[i]
            if inputList[i] > largestNum:
                largestNum = inputList[i]
            if totSum == numToFind:
                return (smallestNum, largestNum)
            elif totSum > numToFind:
                break
            i += 1
        startIndex+= 1
    return "notFound"

inputList = []
rollingList = []
rollingMaxLen = 25
preambleLen = 25
lineCount = 0
invalidNum = -1
with open("input.txt") as file_in:
    for line in file_in:
        line = int(line.rstrip())
        inputList.append(line)
        if lineCount < preambleLen:
            rollingList.append(line)
        else:
            if not determineValidNumber(rollingList, line):
                invalidNum = line
            if len(rollingList) == rollingMaxLen:
                rollingList.pop(0)
            rollingList.append(line)
        lineCount += 1


(startIndex, endIndex) = findContiguousInterval(inputList, invalidNum)
print(startIndex +  endIndex)



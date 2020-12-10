


def determineValidNumber(rollingList, num):
    for x in rollingList:
        for y in rollingList:
            if x + y == num:
                return True
    return False



def findContiguousInterval(inputList, numToFind):
    startIndex = 0

    totSum = 0
    i = startIndex
    while i < len(inputList):
        totSum += inputList[i]
        while totSum > numToFind:
            totSum -= inputList[startIndex]
            startIndex += 1
        if totSum == numToFind:
            print( (startIndex, i))
            return (startIndex, i)
        i += 1
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
                print(lineCount)
                invalidNum = line
            if len(rollingList) == rollingMaxLen:
                rollingList.pop(0)
            rollingList.append(line)
        lineCount += 1


(startIndex, endIndex) = findContiguousInterval(inputList, invalidNum)
newList = inputList[startIndex: endIndex + 1]
maxVal = max(newList)
minVal = min(newList)
print(minVal+ maxVal)



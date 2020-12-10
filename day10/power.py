

def findJoltDiff(inputList):
    joltDiffCount = [0, 0, 0, 0]
    curJoltCount = 0
    for adapter in inputList:
        diff = adapter - curJoltCount
        if diff <= 3  and diff > 0:
            joltDiffCount[diff] += 1
            curJoltCount += diff
            print(joltDiffCount, diff)
        else:
            raise ValueError("can't use all adapters, diff: " + diff + ", adapter: " + adapter)

    # max adapter jolttage:
    diff = 3
    joltDiffCount[diff] += 1
    curJoltCount += diff
    return (joltDiffCount[1], joltDiffCount[3])



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
with open("input.txt") as file_in:
    for line in file_in:
        line = int(line.rstrip())
        inputList.append(line)

inputList.sort()
jolt1, jolt3 = findJoltDiff(inputList)
print(jolt1 * jolt3)



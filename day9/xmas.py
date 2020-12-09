


def determineValidNumber(rollingList, num):
    for x in rollingList:
        for y in rollingList:
            if x + y == num:
                return True
    return False


rollingList = []
rollingMaxLen = 25
preambleLen = 25
lineCount = 0
with open("input.txt") as file_in:
    for line in file_in:
        line = int(line.rstrip())
        if lineCount < preambleLen:
            rollingList.append(line)
        else:
            if not determineValidNumber(rollingList, line):
                print(line)
                exit()
            if len(rollingList) == rollingMaxLen:
                rollingList.pop(0)
            rollingList.append(line)
        lineCount += 1


import math



def calcUniqInGroup(members):
    answers = dict()
    for member in members:
        for answer in member:
            answers[answer] = 1
    return len(answers)








groups = []
with open("input.txt") as file_in:
    group = []
    for line in file_in:
        if line == "\n":
            groups.append(group)
            group = []
        else:
            group.append(line.strip())
    if group:
        groups.append(group)
uniqSum = 0
for group in groups:
    uniqSum += calcUniqInGroup(group)

print(uniqSum)

import math



def calcUniqInGroup(members):
    answers = dict()
    for member in members:
        for answer in member:

            if answer in answers:
                answers[answer] += 1
            else:
                answers[answer] = 1

    numGroupMembers = len(members)
    correctAnswers = 0
    for value in answers.values():
        if value == numGroupMembers:
            correctAnswers += 1
    return correctAnswers







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

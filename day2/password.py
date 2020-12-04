
input_lines = []
with open("input.txt") as file_in:
    for line in file_in:
        input_lines.append(line)


valid_pws = 0

for line in input_lines:
    (policy, token, password) = line.split()
    token = token[0]
    (index1, index2) = policy.split('-')
    index1 = int(index1) - 1
    index2 = int(index2) - 1


    count = 0
    if len(password) >= index2:
        if password[index1] == token:
            count += 1
        if password[index2] == token:
            count += 1

    if count == 1:
       valid_pws += 1



print(valid_pws)

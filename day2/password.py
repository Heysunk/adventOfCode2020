
input_lines = []
with open("input.txt") as file_in:
    for line in file_in:
        input_lines.append(line)


valid_pws = 0

for line in input_lines:
    (policy, token, password) = line.split()
    token = token[0]
    (minLen, maxLen) = policy.split('-')

    count = 0
    for char in password:
        if char == token:
            count += 1

    if count >= int(minLen) and  count <= int(maxLen):
       valid_pws += 1



print(valid_pws)

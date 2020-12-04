



nums = []
with open("input.txt") as file_in:
    for line in file_in:
        nums.append(int(line.strip()))


for num in nums:
    for innerNum in nums:
        if num + innerNum == 2020:
            print(num * innerNum)
            exit()

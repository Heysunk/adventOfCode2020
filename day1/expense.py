



nums = []
with open("input.txt") as file_in:
    for line in file_in:
        nums.append(int(line.strip()))


for num in nums:
    for secNum in nums:
        for triNum in nums:
            if num + secNum + triNum == 2020:
                print(num * secNum * triNum)
                exit()

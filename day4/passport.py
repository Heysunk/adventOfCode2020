import re

reqFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


hclRegex = re.compile('^#[0-9a-f]{6}$')
eclRegex = re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$')
pidRegex = re.compile('^[0-9]{9}$')

def verifyNumRange(low,high, num):
    num = int(num)
    return (num >= low and num <= high)


def validatePassport(entries):

    fields = dict()
    for entry in entries:
        (key, value) = entry.split(':')
        fields[key] = value


    for reqField in reqFields:
        if reqField not in fields:
            return False

    if not verifyNumRange(1920, 2002, fields["byr"]):
        return False
    if not verifyNumRange(2010, 2020, fields["iyr"]):
        return False
    if not verifyNumRange(2020, 2030, fields["eyr"]):
        return False
    hgtVal = fields["hgt"]
    if hgtVal[-2:] == "cm":
        if not verifyNumRange(150,193,int(hgtVal[:-2])):
            return False
    elif hgtVal[-2:] == "in":
        if not verifyNumRange(59,76,int(hgtVal[:-2])):
            return False
    else:
        return False
    if not hclRegex.match(fields["hcl"]):
        return False
    if not eclRegex.match(fields["ecl"]):
        return False
    if not pidRegex.match(fields["pid"]):
        return False
    return True


passports = []
with open("input.txt") as file_in:
    passport = []
    for line in file_in:
        # end of current passport
        if line == "\n":
            passports.append(passport)
            passport = []
        else:
            for entry in line.split():
                passport.append(entry)
    if passport:
        passports.append(passport)


validPassports = 0

for passport in passports:
    if validatePassport(passport):
        validPassports += 1


print(validPassports)

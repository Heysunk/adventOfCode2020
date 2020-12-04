

reqFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def validatePassport(entries):

    fields = dict()
    for entry in entries:
        (key, value) = entry.split(':')
        fields[key] = value


    for reqField in reqFields:
        if reqField not in fields:
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

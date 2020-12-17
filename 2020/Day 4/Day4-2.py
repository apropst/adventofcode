import re
with open('Data4-1.txt', 'r') as myfile:
	filedata = myfile.read().splitlines()

fieldcount = 0
fieldlist = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
solution = 0
index = 0
filelength = len(filedata)
ecllist = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def evalField(field, value):
    if (field == "byr"):
        if ((int(value) >= 1920) and (int(value) <= 2002)):
            return True
        return False
    elif (field == "ecl"):
        for ecl in ecllist:
            if (value == ecl):
                return True
        return False
    elif (field == "eyr"):
        if ((int(value) >= 2020) and (int(value) <= 2030)):
            return True
        return False
    elif (field == "hcl"):
        if re.search("#[0-9a-f]{6}", value):
            return True
        return False
    elif (field == "hgt"):
        measure = value[-2:]
        height = value[:-2]
        if (measure == "in"):
            if ((int(height) >= 59) and (int(height) <= 76)):
                return True
        elif (measure == "cm"):
            if ((int(height) >= 150) and (int(height) <= 193)):
                return True
        return False
    elif (field == "iyr"):
        if ((int(value) >= 2010) and (int(value) <= 2020)):
            return True
        return False
    elif (field == "pid"):
        if re.search("[0-9]{9}", value):
            return True
        return False
    return False

for line in filedata:
    index += 1

    if (line != ""):
        for field in line.split(" "):
            fieldname = field.split(":")[0]
            fieldvalue = field.split(":")[1]
            for listvalue in fieldlist:
                if (fieldname == listvalue):
                    if (evalField(fieldname, fieldvalue)):
                        fieldcount += 1

    if ((index == filelength) or (line == "")):
        if (fieldcount == 7):
            solution += 1
        fieldcount = 0

print("Solution is: " + str(solution))
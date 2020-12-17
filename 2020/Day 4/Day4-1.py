with open('Data4-1.txt', 'r') as myfile:
	filedata = myfile.read().splitlines()

fieldcount = 0
fieldlist = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
solution = 0
index = 0
filelength = len(filedata)

for line in filedata:
    index += 1
    if (line != ""):
        for field in line.split(" "):
            fieldname = field.split(":")[0]
            fieldvalue = field.split(":")[1]
            for listvalue in fieldlist:
                if (fieldname == listvalue):
                    fieldcount += 1
    if ((index == filelength) or (line == "")):
        if (fieldcount == 7):
            solution += 1
        fieldcount = 0

print("Solution is: " + str(solution))
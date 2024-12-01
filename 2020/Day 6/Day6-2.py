import re
with open('Data6-1.txt', 'r') as myfile:
	filedata = myfile.read().splitlines()

solution = 0
index = 0
filelength = len(filedata)
chararr = []
percount = 0
groupstr = ""

for line in filedata:
    index += 1
    if (line != ""):
        percount += 1
        for char in line:
            chararr.append(char)
    if ((index == filelength) or (line == "")):
        chararr.sort()
        for char in chararr:
            groupstr += char
        result = re.findall(r'((\w)\2{' + str((percount - 1)) +'})', groupstr)
        solution += len(result)
        chararr = []
        percount = 0
        groupstr = ""

print("Solution is: " + str(solution))
with open('Data6-1.txt', 'r') as myfile:
	filedata = myfile.read().splitlines()

solution = 0
index = 0
filelength = len(filedata)
chararr = []

for line in filedata:
    index += 1
    if (line != ""):
        for char in line:
            if char not in chararr:
                chararr.append(char)
    if ((index == filelength) or (line == "")):
        solution += len(chararr)
        chararr = []

print("Solution is: " + str(solution))
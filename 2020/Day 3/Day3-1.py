with open('Data3-1.txt', 'r') as myfile:
	filedata = myfile.read().splitlines()

w, h = 31, 323
Matrix = [[0 for x in range(w)] for y in range(h)]
solution = 0
yindex = 0

for line in filedata:
    xindex = 0
    for char in line:
        Matrix[yindex][xindex] = char
        xindex += 1
    yindex += 1

for y in range(h):
    if (y != 0):
        x = (y * 3) % 31
        if (Matrix[y][x] == '#'):
            solution += 1

print("Solution is: " + str(solution))
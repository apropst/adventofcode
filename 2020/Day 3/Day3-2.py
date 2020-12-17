with open('Data3-1.txt', 'r') as myfile:
	filedata = myfile.read().splitlines()

w, h = 31, 323
Matrix = [[0 for x in range(w)] for y in range(h)]
yindex = 0

for line in filedata:
    xindex = 0
    for char in line:
        Matrix[yindex][xindex] = char
        xindex += 1
    yindex += 1

xinc = [1, 3, 5, 7, 1]
yinc = [1, 1, 1, 1, 2]
solutionfinal = 1

for index in range(5):
    y = 0
    x = 0
    solution = 0
    while y < 322:
        y += yinc[index]
        x += xinc[index]
        x = x % 31
        if (Matrix[y][x] == '#'):
            solution += 1
    print("Right " + str(xinc[index]) + ", Left " + str(yinc[index]) + ": " + str(solution))
    solutionfinal = solutionfinal * solution

print("Solution is: " + str(solutionfinal))
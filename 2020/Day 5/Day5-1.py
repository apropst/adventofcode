import math
with open('Data5-1.txt', 'r') as myfile:
	filedata = myfile.read().splitlines()

solution = 0

for line in filedata:
    rowstr = line[:7]
    columnstr = line[-3:]
    rowmin = 0
    rowmax = 127
    seatmin = 0
    seatmax = 7

    for char in rowstr:
        if (char == "F"):
            rowmax = rowmax - math.ceil((rowmax - rowmin) / 2)
        else:
            rowmin = rowmin + math.ceil((rowmax - rowmin) / 2)
    
    for char in columnstr:
        if (char == "L"):
            seatmax = seatmax - math.ceil((seatmax - seatmin) / 2)
        else:
            seatmin = seatmin + math.ceil((seatmax - seatmin) / 2)
    
    seatid = (rowmin * 8) + seatmin

    if (seatid > solution):
        solution = seatid

print("Solution is: " + str(solution))
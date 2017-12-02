inputstring = input("Enter input: ")
inputarray = inputstring.split(", ")
dir = 0
currX = 0
currY = 0
for coord in inputarray:
	if coord[:1] == 'L':
		dir = dir - 90
	elif coord[:1] == 'R':
		dir = dir + 90
	dir = dir % 360
	if dir == 0:
		currY = currY + int(coord[1:])
	elif dir == 90:
		currX = currX + int(coord[1:])
	elif dir == 180:
		currY = currY - int(coord[1:])
	elif dir == 270:
		currX = currX - int(coord[1:])
distance = abs(currX) + abs(currY)
print("Distance to HQ: " + str(distance))
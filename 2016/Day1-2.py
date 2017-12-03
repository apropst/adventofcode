def distfind():
	inputstring = input("Enter input: ")
	inputarray = inputstring.split(", ")
	dir = 0
	currX = 0
	currY = 0
	locations = ['0,0']
	found = 0
	for coord in inputarray:
		if coord[:1] == 'L':
			dir = dir - 90
		elif coord[:1] == 'R':
			dir = dir + 90
		dir = dir % 360
		dist = int(coord[1:])
		for i in range(dist):
			if dir == 0:
				currY = currY + 1
			elif dir == 90:
				currX = currX + 1
			elif dir == 180:
				currY = currY - 1
			elif dir == 270:
				currX = currX - 1
			for location in locations:
				if location == str(currX) + ',' + str(currY):
					distance = abs(currX) + abs(currY)
					return distance
			locations.append(str(currX) + ',' + str(currY))

print("Distance to HQ: " + str(distfind()))
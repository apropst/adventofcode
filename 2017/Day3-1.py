def distfind():
	inputstring = 368078
	oldarea = 1
	axis = 1
	
	for i in range(368078):
		axis = axis + 2
		newarea = axis ** 2
		min = oldarea + 1
		if (min <= inputstring) and (newarea >= inputstring):
			break
		oldarea = newarea
	
	sideindex = 2
	currX = int(axis / 2)
	currY = (int(axis / 2) * -1) + 1
	numindex = min
	
	for i in range(4):
		while sideindex < axis:
			if numindex == inputstring:
				return(abs(currX) + abs(currY))
			if i == 0:
				currY += 1
			if i == 1:
				currX -= 1
			if i == 2:
				currY -= 1
			if i == 3:
				currX += 1
			sideindex += 1
			numindex += 1
		sideindex = 1
	return
	
print("Steps required: " + str(distfind()))
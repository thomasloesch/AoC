INPUT_FILE = "Day2.txt"
LEFT_SIDE   = [1, 2, 5,  10, 13]
RIGHT_SIDE  = [1, 4, 9,  12, 13]
TOP_SIDE    = [1, 2, 4,   5,  9]
BOTTOM_SIDE = [5, 9, 10, 12, 13]

ROWS = [[1], [2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12], [13]]
COLUMNS = [[5], [2, 6, 10], [1, 3, 7, 11, 13] ,[4, 8, 12] ,[9]]

f = open(INPUT_FILE, 'r')
inString = f.read()
f.close()

curr = 5

for s in inString:
	if s == 'U':
		if curr in TOP_SIDE:
			continue
			
		if curr in ROWS[1] or curr in ROWS[4]:
			curr -= 2
		else:
			curr -= 4

	elif s == 'D':
		if curr in BOTTOM_SIDE:
			continue
			
		if curr in ROWS[0] or curr in ROWS[3]:
			curr += 2
		else:
			curr += 4

	elif s == 'L':
		if curr in LEFT_SIDE:
			continue
		curr -= 1

	elif s == 'R':
		if curr in RIGHT_SIDE:
			continue
		curr += 1

	elif s == '\n':
		print(format(curr, 'x'))
	else:
		print("Unexpected character encountered, ignoring")
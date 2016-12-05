INPUT_FILE = "Day2.txt"
LEFT_SIDE   = [1, 4, 7]
RIGHT_SIDE  = [3, 6, 9]
TOP_SIDE    = [1, 2, 3]
BOTTOM_SIDE = [7, 8, 9]

f = open(INPUT_FILE, 'r')
inString = f.read()
f.close()

curr = int('5', base = 16)

for s in inString:
	if s == 'U':
		if curr in TOP_SIDE:
			continue
		curr -= 3

	elif s == 'D':
		if curr in BOTTOM_SIDE:
			continue
		curr += 3

	elif s == 'L':
		if curr in LEFT_SIDE:
			continue
		curr -= 1

	elif s == 'R':
		if curr in RIGHT_SIDE:
			continue
		curr += 1

	elif s == '\n':
		print(curr)
	else:
		print("Unexpected character encountered, ignoring")
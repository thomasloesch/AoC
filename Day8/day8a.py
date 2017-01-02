# Constants
INPUT_FILE = "test.txt"
HEIGHT = 6
WIDTH = 50

# Make 2d list (uses constants HEIGHT and WIDTH defined above)
a = []
for row in range(HEIGHT): a += [['.']*WIDTH]


f = open(INPUT_FILE, 'r')

# Parse through the file line by line
for line in f:
	# Break line into individual tokens
	tokens = line.rstrip().split(' ')
	
	# Determine which action is being taken
	if tokens[0] == "rect":
		# Create a rectangle
		dimensions = tokens[1].split('x')
		x = 0
		y = 0
		print ("Creating a {} rectangle".format(dimensions))
		while x < int(dimensions[0]):
			while y < int(dimensions[1]):
				print("changing {}, {} to #".format(x, y))
				a[y][x] = '#'
				y += 1
			x += 1
		
	elif tokens[0] == "rotate":
		# Check next word for row or column
		if tokens[1] == "row":
			# Trim first two chars (redunant)
			r = tokens[2].split('=')[1]
			
		elif tokens[1] == "column":
			# Trim first two chars (redunant)
			r = tokens[2].split('=')[1]
		
		else:
			print("Unexpected token " + tokens[1] + ": Expected 'row' or 'column'. Aborting.")
			sys.exit()
	
	else:
		print("Unexpected token " + tokens[0] + ": Expected 'rect' or 'rotate'. Aborting.")
		sys.exit()
		
	print(tokens)
	
# Print 2d list
for row in a:
	print(row)
	
f.close()

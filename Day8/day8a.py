# Constants
INPUT_FILE = "input.txt"
HEIGHT = 6
WIDTH = 50

# Make 2d list (uses constants HEIGHT and WIDTH defined above)
a = []
for row in range(HEIGHT): a += [['.'] * WIDTH]


f = open(INPUT_FILE, 'r')

# Parse through the file line by line
for line in f:
	# Break line into individual tokens
	tokens = line.rstrip().split(' ')
		
	print(tokens)
	
	# Determine which action is being taken
	if tokens[0] == "rect":
		# Create a rectangle
		dimensions = tokens[1].split('x')
		x = 0
		print ("Creating a {} rectangle".format(dimensions))
		while x < int(dimensions[0]):
			y = 0
			while y < int(dimensions[1]):
				a[y][x] = '#'
				y += 1
			x += 1
		
	elif tokens[0] == "rotate":
		# Check next word for row or column
		if tokens[1] == "row":
			# Trim first two chars (redunant)
			r = int(tokens[2].split('=')[1])
			
			i = 0
			while i < int(tokens[4]):
				
				j = WIDTH - 1
				#print("{}: {}".format("START", a[r]))
				while j > 0:
					
					temp = a[r][j]
					a[r][j] = a[r][j - 1]
					a[r][j - 1] = temp
					#print("{}: {}".format(j, a[r]))
					j -= 1
				
				#temp = a[r][0]
				#a[r][0] = a[r][WIDTH - 1]
				#a[r][WIDTH - 1] = temp
				#print("{}: {}".format(j, a[r]))
				i += 1
			
		elif tokens[1] == "column":
			# Trim first two chars (redunant)
			r = int(tokens[2].split('=')[1])
			
			i = 0
			while i < int(tokens[4]):
				#print("i: {}".format(i))
				j = HEIGHT - 1
				while j > 0:
					#print("j: {}".format(j))
					temp = a[j][r]
					a[j][r] = a[j - 1][r]
					a[j - 1][r] = temp
					j -= 1
				
				#temp = a[0][r]
				#a[0][r] = a[HEIGHT - 1][r]
				#a[HEIGHT - 1][r] = temp
				i += 1
				
		else:
			print("Unexpected token " + tokens[1] + ": Expected 'row' or 'column'. Aborting.")
			sys.exit()
	
	else:
		print("Unexpected token " + tokens[0] + ": Expected 'rect' or 'rotate'. Aborting.")
		sys.exit()
	
# Print 2d list
total = 0
for row in a:
	total += row.count('#')
	print(row)
	
# Get count
print(total)
	
f.close()

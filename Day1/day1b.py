# Constants
NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3
READ_FILE = 'day1a.txt'

# Functions
# Takes a char (L or R) and an int (dir) and returns the new dir
def rotate( rotation, dir ):
	if rotation == 'L':
		dir -= 1;
	elif rotation == 'R':
		dir += 1
		
	return dir;

# Open and read values from file
f = open(READ_FILE, 'r')
moves = f.read().rsplit(',')

# Initialihe vars to store (x, y) position and current direction
xPos = 0
yPos = 0
dir = NORTH

# Initialize list to store previously visited locations
visited = []
dupes = []

# Iterates through the list and changes the values of xPos and yPos accordingly
for i in moves:
	temp = i.lstrip(' ')
	dir = rotate(temp[0], dir) % 4
	
	temp = temp.lstrip('L')
	temp = temp.lstrip('R')
	
	if dir == NORTH:
		for h in range(int(temp)):
			if (xPos, yPos + h) in visited:
				dupes.append((xPos, yPos + h))
			visited.append((xPos, yPos + h))
		yPos += int(temp)
	elif dir == EAST:
		for h in range(int(temp)):
			if (xPos + h, yPos) in visited:
				dupes.append((xPos + h, yPos))
			visited.append((xPos + h, yPos))
		xPos += int(temp)
	elif dir == SOUTH:
		for h in range(int(temp)):
			if (xPos, yPos - h) in visited:
				dupes.append((xPos, yPos - h))
			visited.append((xPos, yPos - h))
		yPos -= int(temp)
	else:
		for h in range(int(temp)):
			if (xPos - h, yPos) in visited:
				dupes.append((xPos - h, yPos))
			visited.append((xPos - h, yPos))
		xPos -= int(temp)
	
answer = abs(xPos) + abs(yPos)
answer2 = abs(dupes[0][0]) + abs(dupes[0][1])
	
print(visited)
print()
print(dupes)
print(answer)
print(answer2)
	

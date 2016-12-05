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

# Initialize vars to store (x, y) position and current direction
xPos = 0
yPos = 0
dir = NORTH

# Iterates through the list and changes the values of xPos and yPos accordingly
for i in moves:
	temp = i.lstrip(' ')
	dir = rotate(temp[0], dir) % 4
	
	temp = temp.lstrip('L')
	temp = temp.lstrip('R')
	
	if dir == NORTH:
		yPos += int(temp)
	elif dir == EAST:
		xPos += int(temp)
	elif dir == SOUTH:
		yPos -= int(temp)
	else:
		xPos -= int(temp)
	
answer = abs(xPos) + abs(yPos)
	
print(answer)
	

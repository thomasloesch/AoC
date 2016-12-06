FILE_NAME = "Day3.txt"

def CheckTri(t):
	print("Checking triangle " + str(t))
	print("Side 1 + 2: " + str(t[0] + t[1]))
	if (t[0] + t[1]) <= t[2]:
		return False
	print("Side 2 + 3: " + str(t[1] + t[2]))
	if (t[1] + t[2]) <= t[0]:
		return False
	print("Side 1 + 3: " + str(t[0] + t[2]))
	if (t[0] + t[2]) <= t[1]:
		return False
	return True

f = open(FILE_NAME, 'r')
inStr = f.read()
f.close();

data = []

inStr = inStr.strip('\n').lstrip(' ')

while inStr != '':
	part = inStr.partition(' ')
	int1 = int(part[0])
	part = part[2].lstrip(' ').partition(' ')
	int2 = int(part[0])
	part = part[2].lstrip(' ').partition(' ')
	int3 = int(part[0])

	data.append((int1, int2, int3))

	inStr = part[2].lstrip()

print (data[0][0])
print (data[0][1])
print (data[0][2])

i = 0
for t in data:
	if CheckTri(t):
		i += 1

print(i)
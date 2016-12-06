FILE_NAME = "Day3.txt"

def CheckTri(t):
	if (t[0] + t[1]) <= t[2]:
		return False
	if (t[1] + t[2]) <= t[0]:
		return False
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

print (len(data))

data2 = []
i = 0
while i < len(data):
	data2.append((data[i][0], data[i + 1][0], data[i + 2][0]))
	data2.append((data[i][1], data[i + 1][1], data[i + 2][1]))
	data2.append((data[i][2], data[i + 1][2], data[i + 2][2]))
	i += 3

total = 0
for t in data2:
	if CheckTri(t):
		total += 1

print(total)
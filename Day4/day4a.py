import string

FILE_NAME = "day4.txt"

def GetTopFive( name ):
	d = dict.fromkeys(string.ascii_lowercase, 0)
	
	for c in name.replace('-', ''):
		d[c] += 1
		
	retval = ""
	i = 0
	while i < 5:
		highestSoFar = ('' ,-1) 
		for e in sorted(d.items()):
			if(e[1] > highestSoFar[1]):
				highestSoFar = e + tuple()
		
		del d[highestSoFar[0]]
		retval += highestSoFar[0]
		i += 1
		
	return retval
	
def Decypher( name, id ):
	retval = ""

	i = 0
	while i < len(name):
		if name[i] == "-":
			retval += " "
		else:
			temp = ord(name[i]) - 97
			temp += id
			temp %= 26
			retval += chr(97 + temp)
		
		i += 1
	return retval

f = open(FILE_NAME, 'r')
inStr = f.read()
f.close()

data = inStr.split('\n')
total = 0
for s in data:
	# Split each input line into name, id, and check
	part = s.partition('[')
	check = part[2].strip(']')
	part = part[0].rpartition('-')
	id = int(part[2])
	name = part[0]
	
	if GetTopFive(name) == check:
		print("{}: {}".format(Decypher(name, id), id))

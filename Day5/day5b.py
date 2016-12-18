import hashlib

INPUT = "reyedfim"

def CheckForFiveZeroes( s ):
	i = 0
	while i < 5:
		if s[i] != '0':
			return False
		i += 1
	return True

def BetweenZeroAndSeven( c ):
	return ord(c) in range(ord('0'), ord('8'))

out = ""

passDict = { '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None }

j = 0
while len(out) < 8:
	m = hashlib.md5()
	m.update((INPUT + str(j)).encode('utf-8'))

	s = m.hexdigest()
	#print("{}{}: {}".format(INPUT, j, s))
	if(CheckForFiveZeroes(s)):
		msg = "ERROR"
		if(BetweenZeroAndSeven(s[5])):
			if(passDict[s[5]] == None):
				passDict[s[5]] = s[6]
				msg = "Added"
				out += s[6]
			else:
				msg = "Already found, skipping"
		else:
			msg = "Not a valid position, skipping"
		print("{}\t{}: {};\t".format(j, s[5], s[6]) + msg)
	j += 1

print(passDict['0'] + passDict['1'] + passDict['2'] + passDict['3'] + passDict['4'] + passDict['5'] + passDict['6'] + passDict['7'])
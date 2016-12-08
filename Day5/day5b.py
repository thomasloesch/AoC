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
	return ord(c) in range(ord('0'), ord('7'))

out = ""

passDict = { '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None }

j = 0
while len(out) < 8:
	m = hashlib.md5()
	m.update(INPUT + str(j))

	s = m.hexdigest()
	#print("{}{}: {}".format(INPUT, j, s))
	if(CheckForFiveZeroes(s))
		out += s[5]
		print("{}: {}".format(len(out), s[5]))
	j += 1

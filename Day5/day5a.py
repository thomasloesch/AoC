import hashlib

INPUT = "reyedfim"

out = ""

j = 0
while len(out) < 8:
	m = hashlib.md5()
	m.update(INPUT + str(j))

	s = m.hexdigest()
	#print("{}{}: {}".format(INPUT, j, s))
	i = 0
	while i < 5:
		if s[i] != '0':
			break
		i += 1
	if i == 5:
		out += s[5]
		print("{}: {}".format(len(out), s[5]))
	j += 1

print("Answer: " + out)

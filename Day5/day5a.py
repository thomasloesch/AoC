import hashlib

INPUT = "reyedfim"

out = ""

j = 0
while len(out) < 8:
	m = hashlib.md5()
	m.update(INPUT + chr(j))

	s = m.hexdigest()[5]
	print(s)
	i = 0
	while i < 6:
		if s[i] != '0':
			i += 1
			break
		i += 1
		print(s[5])
	j += 1

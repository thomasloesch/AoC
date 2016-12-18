import string
import math

FILE_NAME = "day6.txt"

f = open(FILE_NAME, 'r')
rows = [[], [], [], [], [], [], [], []]

for line in f:
	rows[0].append(line[0])	
	rows[1].append(line[1])
	rows[2].append(line[2])
	rows[3].append(line[3])
	rows[4].append(line[4])
	rows[5].append(line[5])
	rows[6].append(line[6])
	rows[7].append(line[7])	

for l in rows:
	d = dict.fromkeys(string.ascii_lowercase, 0)
	for c in l:
		d[c] += 1

	m = float("inf")
	mKey = ""
	for t in d:
		if d[t] < m:
			m = d[t]
			mKey = t

	print (mKey)


f.close()
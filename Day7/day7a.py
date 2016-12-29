INPUT_FILE = "input.txt"

f = open(INPUT_FILE, 'r')
found = 0

for line in f:
	brackets = False
	temp = 0
	i = 0
	while i < len(line) - 4:
		chunk = line[i:i + 4]
		if chunk[0] == '[':
			brackets = True
		elif chunk[0] == ']':
			brackets = False
		
		elif '[' not in chunk and ']' not in chunk:
			if chunk[0] != chunk[1] and chunk[0] == chunk[3] and chunk[1] == chunk[2]:
				if brackets == False:
					if temp < 1:
						temp += 1
					print("FOUND " + chunk)
				elif brackets == True:
					print("FOUND " + chunk + " but []")
					temp = 0
					break
		i += 1
	found += temp
	
print(found)
	
f.close()
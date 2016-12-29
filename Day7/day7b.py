INPUT_FILE = "input.txt"

f = open(INPUT_FILE, 'r')
found = 0

for line in f:
	accessor = []
	allocation = []

	brackets = False
	temp = 0
	i = 0
	while i < len(line) - 3:
		chunk = line[i:i + 3]
		if chunk[0] == '[':
			brackets = True
		elif chunk[0] == ']':
			brackets = False
		
		elif '[' not in chunk and ']' not in chunk:
			if chunk[0] != chunk[1] and chunk[0] == chunk[2]:
				# Add to lists depending on brackets
				if brackets:
					allocation.append(chunk)
				else:
					accessor.append(chunk)
		i += 1
	
	for s in accessor:
		reverse = s[1] + s[0] + s[1]
		if reverse in allocation:
			found += 1
			break
	
print(found)
	
f.close()
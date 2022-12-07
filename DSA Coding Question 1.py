lastNumber = 5
alphabet = 65

for i in range(0, lastNumber):
	for j in range(0, i+1):
		ch = chr(alphabet)
		print(ch, end=" ")
	alphabet += 1
	print("")
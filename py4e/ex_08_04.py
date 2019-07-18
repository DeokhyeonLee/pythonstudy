fname = input('Enter file : ')

try :
	fhand = open(fname)
except :
	print('file can not be fined, ', fname)
	quit()

lst = list()

for line in fhand:
	newline = line.split()
	lst.append(words)
	#words.sort()

print(line.rstrip())


fhand = open('mbox-short.txt')

for line in fhand:
	line = line.rstrip()

	wds = line.split()
	# Guardian pattern
	if len(wds) < 3 or wds[0] != 'From' : =
		# print('Ignore')
		continue
	print(wds[2])
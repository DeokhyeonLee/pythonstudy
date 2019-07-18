fhand = open('test.txt')

for line in fhand:
	line = line.rstrip() #오른쪽 공백 제거
	#if line.startswith('air')
	print(line)


fname = input('Enter the file name: ')

try:
	fhand = open(fname)
except:
	print('File cannot be opended : ', fname)
	quit()

count = 0
for line in fhand:
	if line.startswith('air'):
		count += 1

print('There were',count,'air lines in ', fname)

fhand = opne('mbox-short.txt')

for line in fhand:
	line
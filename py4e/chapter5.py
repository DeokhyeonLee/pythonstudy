n = 5
while n > 0:
	print(n)
	n = n -1

print('Blasoff!')
print(n)


while True:
	line = input('> ')
	if line[0] == '#':
		continue	#이번회차의 실행 멈춤
	if line == 'done' :
		break	#조건이 맞는 순간 루프 종료
	print(line)

print('Done!')

largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
	if the_num > largest_so_far :
		largest_so_far = the_num
	print(largest_so_far, the_num)
print('After', largest_so_far)

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
	zork += thing
	print(zork, thing)

print('ater', zork)


count = 0
total = 0
print('Before', count, total)
for value in [9, 41, 12, 3, 74, 15]:
	count += 1
	total += value
	print(count, total, value)

print('After', count, total, total/count)


print('Before')
for value in [9, 41, 12, 3, 74, 15]:
	if value > 20:
		print('Large number', value)

print('Ater')



smallest = None
print('Before')
for value in [9,41,12,3,74,15] :
	if smallest is None :
		smallest = value
	elif value < smallest :
		smallest = value
	print(smallest, value)
print('After', smallest)






















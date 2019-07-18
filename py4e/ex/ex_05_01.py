sum1 = 0
count = 0
# avr1 = 0
while True:
	num1 = input("Enter a number : ")
	
	if num1 == 'done':
		break
	try:
		num2 = int(num1)
	except:
		print('Invalid data')
		continue

	sum1 += int(num2)
	count += 1
	#avr1 = sum1 / count

print(sum1, count, sum1 / count)
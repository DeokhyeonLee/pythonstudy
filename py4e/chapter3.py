x = 5
if x < 2 : 
	print('small')
elif x < 10 :
	print('Medium')
else : 		
	print('Large')
print('All done')



# the Try / except Structure
astr = 'Hello Bob'
try : 
	istr = int(astr)
except : 
	istr = -1

print('First', istr)

astr = '123'
try:
	istr = int(astr)
except : 
	istr = -1

print('Second', istr)


#try 블록에는 중단될 것 같은 문장만 넣는 게 좋음.
astr = 'Bob'
try:
	print('hello')
	istr = int(astr)
	print('There')

except:
	istr = -123

print('Done', istr)


#Sample try /except
rawstr = input('Enter a number : ')
try:
	ival = int(rawstr)
except:
	ival = -1

if ival > 0:
	print("Nice work")
else:
	print('not a number')




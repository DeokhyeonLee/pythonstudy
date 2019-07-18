#big = max('Hello world') #영어에서는 소문자 > 대문자
#print(big)

#tiny = min('Hello world') #결과값 출력 X why?
#print(tiny)
x = 5
print('Hello')

def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I Sleep all night and I work all day.')

print('Yo')
print_lyrics()
x = x + 2
print(x)


def greet(lang): #함수에는 retrun을 사용하도록 하자
	if lang == 'es':
		print('Hola')
	elif lang == 'fr':
		print('Bonjour')
	else:
		print('Hello')

greet('en')
greet('es')
greet('fr')

def greet2(lang): #함수에는 retrun을 사용하도록 하자
	if lang == 'es':
		return 'hola'
	elif lang == 'fr':
		return 'Bonjour'
	else:
		return 'Hello'

print(greet2('en'), 'Deok')

#여러 개의 매개변수
def addtwo(a, b): 
	added = a + b
	return added

x = addtwo(3, 5)
print(x)









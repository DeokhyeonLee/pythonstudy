#개만들기 
print('|\\_/|')
print('|q p|   /}')
print('( 0 )\"\"\"\\')
print('|\"^\"`    |')
print('||_/=\\\\__|')


#문제 7287번 - 맞은 문제 개수 출력
print('7\nfatum')


# lambda, map 함수 사용!!!
#문제 1000번 - 두 정수 입력 받은 후, 합 출력
a, b = map(int, input().split())
print(a+b)

# 문제 1001번 - 두 정수 입력 받은 후, 차 출력
# map을 사용하여 정수로 변환, split의 결과를 모두 int로 변환
# input('기준문자열').split('입력된 값을 기준으로 분리') 변수 여러개 저장

a, b = map(int, input().split()) 
print(a-b)


# 10998번 - 두 수의 곱셈
a, b = map(int, input().split())
print(a*b)

# 1008번
a, b = map(int, input().split())
print(a/b)


#10869번 - 두 자연수의 사칙연산
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b)) #파이썬은 자동 형변환이 이루어짐!
print(a%b)


#2588번 - 두 수의 곱을 차례대로 출력
a, b = map(int, input().split())

temp = b
for value in range(3):
	print((temp%10)*a)
	temp = temp // 10
print(a*b)



















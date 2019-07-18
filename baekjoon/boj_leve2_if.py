# 2588번
a, b = map(int, input().split())
# a = int(input())
# b = int(input())
temp = b
for value in range(3):
	print((temp%10)*a)
	temp = temp // 10
print(a*b)


#10430번

a,b,c = map(int, input().split())
print((a + b) % c)
print((a%c + b%c) % c)
print((a*b)%c)
print((a%c * b%c)%c)



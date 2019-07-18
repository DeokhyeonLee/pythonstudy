# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
# 예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

def solution(s):
	if len(s) == 4 or len(s) == 6:
		try : 
			int(s)

		except : 
			result = False
			return result

		result = True
	else : 
		result = False
	return result

print(solution('a234'))
print(solution('1234'))

hrs = input("Enter Hours : ")

try:
	h = float(hrs)

except:
	print('Error, please enter numeric input')
	quit()

rate = input("Enter Rate : ")

try: 
	r = float(rate)
except:
	print('Error, please enter numeric input')
	quit()

pay = float(hrs) * float(rate)
print("Pay is ",pay)
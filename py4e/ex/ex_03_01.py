hrs = input("Enter Hours : ")
h = float(hrs)
rate = input("Enter Rate : ")
r = float(rate)

pay = h * r
overtimepay = (h - 40.0) * (r * 0.5)

if h > 40:
	otpay = pay + overtimepay
	print('Pay is', otpay)
else:
	print(pay)


def computepay(hours, rate):
    
    if hours > 40:
    	reg_pay = hours * rate
    	otp = (hours - 40.0) * (rate * 0.5)
    	pay = reg_pay + otp
    else:
    	pay = hours * rate
    return pay

a = input('Enter Hours : ')
h = float(a)
b = input('Enter Rate : ')
r = float(b)

x = computepay(h, r)
print("pay is : ",x)
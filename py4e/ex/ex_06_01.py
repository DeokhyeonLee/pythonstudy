str = 'X-DSPAM-Confidence: 0.8475'

x = str.find(':')
#print(x)

y= str[x+2 : ]
print(float(y))




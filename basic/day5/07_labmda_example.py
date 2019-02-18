a = 10
b =20

def calculate(a,b,func):
	a *= 10
	b *= 10
	result = func(a,b)
	return result

result1 = calculate(a,b,lambda x,y:x+y)
result2 = calculate(a,b,lambda x,y:x-y)
result3 = calculate(a,b,lambda x,y:x*y)
result4 = calculate(a,b,lambda x,y:x/y)

print(result1,result2,result3,result4)
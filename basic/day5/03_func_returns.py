def add(a,b):
	return a + b

value = add(10,12)
print(value)


def guess(a):
	if a > 10:
		return "大于10的数"
	elif a < 0:
		return "负数"

val = guess(110)
print(val)

def greet(username,age):
	return username,age

vals = greet("wanghui",23)
print(vals,type(vals))

username,age = greet("wanghui",23)
print(username)
print(age)
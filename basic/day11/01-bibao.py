def greet(name):
	print('outer')
	def say_hello():
		print("hello %s"%name)
	return say_hello

#ret = greet('hahaha')
# ret()
# print(ret)

# def calculator(x,y,operator):
# 	if operator == 1:
# 		return x+y
# 	elif operator == 2:
# 		return x-y
# 	elif operator == 3:
# 		return x*y
# 	elif operator == 4:
# 		return x/y
# 	else:
# 		print ("operator error")


# ret1 = calculator(2,4,1)
# ret1 = calculator(2,4,1)
# ret1 = calculator(2,4,1)
# ret1 = calculator(2,4,1)
# print(ret1)

def calculator(operator):
	if operator == 1:
		def add(x,y):
			return x+y
		return add

	elif operator == 2:
		def minus(x,y):
			return x-y
		return minus

	elif operator == 3:
		def multiply(x,y):
			return x*y
		return multiply

	elif operator == 3:
		def devide(x,y):
			return x/y
		return devide

add = calculator(1)
ret = add(3,6)
print(ret)

multiply = calculator(3)
ret = multiply(9,9)
print(ret)
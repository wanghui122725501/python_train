# NUM = 10
# def add():
# 	global NUM
# 	NUM += 1
# 	print(NUM)

# add()


def greet(name):
	print("OUTER name is %s"%name)
	def say_hello():
		nonlocal name
		name += "hahah"
		print("INNER name is %s"%name)
	return say_hello

ret = greet("wanglex")
ret()

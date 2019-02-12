def add(a,b):
	print(a+b)

add(10,11)
#混合参数的传递，位置参数一定要在关键字参数之前
add(1,b=2)
add(a=1,b=2)
# add(b=2,1)

def add_1(*args):
	result = 0
	for arg in args:
		result += arg
		print(result)
	# print(args)

add_1(1,2,3,4,5,6)


def add_2(**kwargs):
	print(kwargs)

add_2(a=1,b=2,c=3,d=4)



def add_3(*args,**kwargs):
	print(args)
	print(kwargs)

add_3(1,23,4)


def greet(name,age=12):
	print(name,age)

greet("wanghui",13)
greet("xxx")
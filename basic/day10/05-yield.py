

def my_gen():
	a = 1
	yield 1
	yield 2
	yield 3

ret = my_gen()
print(ret)
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))
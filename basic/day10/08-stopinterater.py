def my_gen():
	print('hello')
	yield 1
	return
	yield 2

ret = my_gen()
next(ret)
next(ret)

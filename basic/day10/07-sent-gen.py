

def my_gen(start):
	while start < 10:
		#如果是yield xxx永远返回None
		tmp = yield start
		print(tmp)
		start += 1


ret = my_gen(1)
print(ret.send(None))   #
print(ret.__next__())
print(ret.__next__())
# print(ret.__next__())
print(ret.send('hello'))

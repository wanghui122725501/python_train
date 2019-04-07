

def my_gen(start,end):
	index = start
	while index <= end:
		yield index
		index += 1

ret = my_gen(1,1000000000)
for x in ret:
	print(x)
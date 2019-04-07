from collections import Iterable


class MyRangeIterator(object):
	def __init__(self,start,end):
		self.start = start
		self.end = end

	def __iter__(self):
		return self

	def __next__(self):
		if self.start < self.end:
			temp = self.start
			self.start += 1
			return temp
		else:
			raise StopIteration()

class MyRange(object):
	"""
	myrange是可迭代对象
	"""
	def __init__(self,start,end):
		self.start = start
		self.end = end

	def __iter__(self):
		"""返回可迭代对象"""
		return MyRangeIterator(self.start,self.end)


ret = MyRange(1,10)
for x in ret:
	print(x)
# ret_iterator = iter(ret)
# while True:
# 	try:
# 		x = ret_iterator.__next__()
# 		print(x)
# 	except StopIteration:
# 		break

print("="*30)
for y in ret:
	print(y)
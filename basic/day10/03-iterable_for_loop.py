from collections import Iterable

class MyRange(object):
	"""
	myrange是可迭代对象
	"""
	def __init__(self,start,end):
		self.start = start
		self.end = end
		self.index = start

	def __iter__(self):
		"""返回可迭代对象"""
		return self

	def __next__(self):
		if self.start < self.end:
			temp = self.start
			self.start += 1
			return temp
		else:
			raise StopIteration()

my_range = MyRange(1,10)
for i in my_range:
	print(i)

print("="*30)

for y in my_range:
	print(y)